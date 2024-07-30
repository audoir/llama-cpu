curl http://localhost:8080/v1/chat/completions -H "Content-Type: application/json"   -d '{
  "model": "any-model",
  "messages": [
    {
      "role": "system",
      "content": "You are a coding  assistant, skilled in programming."
    },
    {
      "role": "user",
      "content": "Write a hello world program in C++."
    }
  ]
}' 2>/dev/null | jq -C
