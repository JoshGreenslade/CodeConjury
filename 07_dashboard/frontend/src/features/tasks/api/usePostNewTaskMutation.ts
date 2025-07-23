import { useMutation } from "@tanstack/react-query"
import api from "../../../common/axios"
import type { TasksResponse } from "../types"

type payload = {taskName: string};

export const usePostNewTaskMutation = () => 
  useMutation<TasksResponse, Error, payload>({
    mutationFn: (taskName) => 
      api.post<TasksResponse>(`/todo/new`, {"taskName": taskName})
    .then((res) => res.data),
});