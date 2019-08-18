defmodule Solution do
  use Bitwise

  n = IO.read(:stdio, :line)

  n = n
  |> String.trim()
  |> String.to_integer()

  if ((n &&& 1) == 1) or (6 <= n and n <= 20) do
    IO.puts("Weird")
  else
    IO.puts("Not Weird")
  end
end
