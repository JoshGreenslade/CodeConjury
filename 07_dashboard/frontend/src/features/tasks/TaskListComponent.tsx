import { useState } from "react";
import type { Task } from "./types";
import { useGetTasksMutation } from "./api/useGetTasksMutation";

export const TaskListComponent = () => {
  const { mutate, data, isPending, isError } = useGetTasksMutation();
  const [prompt, setPrompt] = useState("");

  return (
    <div>
      <div>
        <input
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          placeholder="Enter your prompt"
        />
        <button onClick={() => mutate(prompt)}>Fetch Tasks</button>
      </div>

      <div>
        {isPending && <p>Loading...</p>}
        {isError && <p>Failed to get tasks </p>}

        <span>{data?.results.summary}</span>
        <ul>
          {data?.results.recommended.map((task: Task) => (
            <li key={task.task_id}>
              {task.title} - {task.reason} - {task.effort}/10
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};
