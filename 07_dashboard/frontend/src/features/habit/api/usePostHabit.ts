import { useMutation } from "@tanstack/react-query"
import api from "../../../common/axios"
import type { Habit } from "../types"

export const usePostHabit = () => {
  return useMutation({
    mutationFn: (data: Habit) => 
      api.post("/habits/", data),
  })
}