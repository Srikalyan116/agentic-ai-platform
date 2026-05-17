import React, { useEffect, useState } from 'react';
import { createRoot } from 'react-dom/client';
import { api } from './api';
import './styles.css';

function App() {
  const [tasks, setTasks] = useState([]);
  const [dashboard, setDashboard] = useState({ total: 0, pending: 0, in_progress: 0, completed: 0 });
  const [form, setForm] = useState({ title: '', description: '', owner: '', status: 'Pending', complexity: 1, business_impact: 1 });

  const loadData = async () => {
    const [taskRes, dashRes] = await Promise.all([api.get('/tasks'), api.get('/dashboard')]);
    setTasks(taskRes.data);
    setDashboard(dashRes.data);
  };

  useEffect(() => { loadData(); }, []);

  const submitTask = async (e) => {
    e.preventDefault();
    await api.post('/tasks', form);
    setForm({ title: '', description: '', owner: '', status: 'Pending', complexity: 1, business_impact: 1 });
    loadData();
  };

  const deleteTask = async (id) => {
    await api.delete(`/tasks/${id}`);
    loadData();
  };

  return (
    <main className="page">
      <section className="hero">
        <div>
          <p className="eyebrow">AI-FIRST FULL STACK PROJECT</p>
          <h1>Workflow Intelligence Dashboard</h1>
          <p>Manage engineering tasks, REST APIs, database records, and AI-style priority recommendations in one responsive platform.</p>
        </div>
      </section>

      <section className="stats">
        <div><span>{dashboard.total}</span><p>Total Tasks</p></div>
        <div><span>{dashboard.pending}</span><p>Pending</p></div>
        <div><span>{dashboard.in_progress}</span><p>In Progress</p></div>
        <div><span>{dashboard.completed}</span><p>Completed</p></div>
      </section>

      <section className="grid">
        <form className="card" onSubmit={submitTask}>
          <h2>Create Task</h2>
          <input placeholder="Task title" value={form.title} onChange={e => setForm({ ...form, title: e.target.value })} required />
          <textarea placeholder="Description" value={form.description} onChange={e => setForm({ ...form, description: e.target.value })} />
          <input placeholder="Owner" value={form.owner} onChange={e => setForm({ ...form, owner: e.target.value })} />
          <select value={form.status} onChange={e => setForm({ ...form, status: e.target.value })}>
            <option>Pending</option><option>In Progress</option><option>Completed</option>
          </select>
          <label>Complexity: {form.complexity}</label>
          <input type="range" min="1" max="5" value={form.complexity} onChange={e => setForm({ ...form, complexity: Number(e.target.value) })} />
          <label>Business Impact: {form.business_impact}</label>
          <input type="range" min="1" max="5" value={form.business_impact} onChange={e => setForm({ ...form, business_impact: Number(e.target.value) })} />
          <button>Create Intelligent Task</button>
        </form>

        <div className="card list">
          <h2>Task Board</h2>
          {tasks.map(task => (
            <article className="task" key={task.id}>
              <div>
                <h3>{task.title}</h3>
                <p>{task.description || 'No description added'}</p>
                <small>{task.owner} · {task.status}</small>
              </div>
              <div className="score">
                <strong>{task.ai_priority_score}</strong>
                <span>{task.recommendation}</span>
                <button onClick={() => deleteTask(task.id)}>Delete</button>
              </div>
            </article>
          ))}
        </div>
      </section>
    </main>
  );
}

createRoot(document.getElementById('root')).render(<App />);
