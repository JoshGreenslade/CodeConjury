import { useMutation } from "@tanstack/react-query"
import api from "../../../common/axios"

type HydrationInput = {
  hydration: number;
}

export const usePostHydration = () => {
  return useMutation({
    mutationFn: (data: HydrationInput) => 
      api.post("/hydration/today", data),
  })
}