defmodule Solution do
  n = IO.read(:stdio, :line)
  x = IO.read(:stdio, :line)

  n = n
  |> String.trim()
  |> String.to_integer()

  x = x
  |> String.split(" ")
  |> Enum.map(fn value -> String.to_integer(value) end)
  |> Enum.take(n)
  |> Enum.sort()

  mean = Enum.reduce(x, 0, fn value, acc -> value + acc end) / n
  middle = div(n, 2)

  median = if rem(n, 2) != 0 do
    Enum.at(x, middle)
  else
    (Enum.at(x, middle - 1) + Enum.at(x, middle)) / 2
  end

  [{mode, _} | _] = x
  |> Enum.reduce(
    %{},
  fn value, acc ->
    Map.update(acc, value, 1, fn c -> c + 1 end)
  end
  )
  |> Enum.sort(fn
    {x, a}, {y, b} when a == b -> x <= y
    {_, a}, {_, b} -> a >= b
  end)

  IO.puts(Float.round(mean, 1))
  IO.puts(Float.round(median, 1))
  IO.puts(mode)
end
