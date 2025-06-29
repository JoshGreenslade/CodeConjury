import { useMutation } from "@tanstack/react-query"
import api from "../../../common/axios"
import type { HabitPost } from "../types"

export const usePostHabit = () => {
  return useMutation({
    mutationFn: (data: HabitPost) => 
      api.post("/habits/", data),
  })
}