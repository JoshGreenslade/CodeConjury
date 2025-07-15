import { useState } from "react";
import type { Task } from "./types";
import { useGetTasksMutation } from "./api/useGetTasksMutation";
import { useSetTaskDoneMutation } from "./api/useSetTaskDoneMutation";
import './TaskListComponent.css'

export const TaskListComponent = () => {
  const { mutate: getTasks, data, isPending: getTasksPending, isError: getTasksError } = useGetTasksMutation();
  const { mutate: setTask, isPending: setTaskPending, isError: setTaskError } = useSetTaskDoneMutation();
  const [prompt, setPrompt] = useState("");

  return (
    <div>
      <div>
        <input
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          placeholder="Enter your prompt"
        />
        <button onClick={() => getTasks(prompt)} disabled={getTasksPending}>Fetch Tasks</button>
      </div>

      <div>
        {getTasksPending && <p>Loading...</p>}
        {getTasksError && <p>Failed to get tasks </p>}
        <span>{data?.results.summary}</span>
        {data && (<div className="task-header">
          <span>Title</span>
          <span>Reason</span>
          <span>Effort</span>
          <span>Done</span>
        </div>
        )}
        <ul className="task-list">
          {data?.results.recommended.map((task: Task) => (
            <li key={task.task_id} className="task">
              <span>{task.title}</span>
              <span>{task.reason}</span>
              <span>{task.effort}/10</span>
              <input type="checkbox" className="taskToggle" onChange={(e) => setTask({task_id:task.task_id, completed:e.target.checked}) } />
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};
