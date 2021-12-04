file = File.open("day2.txt")
file_data = file.readlines.map(&:chomp)

x = 0
y = 0
y2 = 0

file_data.each do | i |
    a, b = i.split()
    b = b.to_i
    if a == "forward"
        x += b
        y2 += b * y
    elsif a == "up"
        y -= b
    else
        y += b
    end
end

puts "Part one:", x * y
puts "Part two:", x * y2 