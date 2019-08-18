defmodule Solution do
  use Bitwise

  n = IO.read(:stdio, :line)
  |> String.trim()
  |> String.to_integer()

  Enum.each(1..n, fn _ ->
    line = IO.read(:stdio, :line)
    |> String.trim()
    |> String.graphemes()

    {left, right} = line
    |> Enum.with_index()
    |> Enum.reduce({[], []}, fn {c, index}, {left, right} ->
      if (index &&& 1) == 0 do
        {[c | left], right}
      else
        {left, [c | right]}
      end
    end)

    left = left |> Enum.reverse() |> Enum.join("")
    right = right |> Enum.reverse() |> Enum.join("")

    IO.puts "#{left} #{right}"
  end)
end
