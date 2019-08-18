defmodule Solution do
  n = IO.read(:stdio, :line)
  x = IO.read(:stdio, :line)
  w = IO.read(:stdio, :line)

  n = n
  |> String.trim()
  |> String.to_integer()

  x = x
  |> String.trim()
  |> String.split(" ")
  |> Enum.map(&String.to_integer/1)
  |> Enum.take(n)

  w = w
  |> String.trim()
  |> String.split(" ")
  |> Enum.map(&String.to_integer/1)
  |> Enum.take(n)

  lt = 1..n
  |> Enum.zip(w)
  |> Enum.into(%{})

  x = 1..n
  |> Enum.zip(x)
  |> Enum.reduce(0, fn {index, value}, acc -> acc + value * Map.get(lt, index) end)

  w = Enum.reduce(w, 0, fn value, acc -> acc + value end)

  IO.puts(Float.round(x / w, 1))
end
