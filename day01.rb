file = File.open("day1.txt")
file_data = file.readlines.map(&:to_i)

d = 0 
file_data.each_with_index do | val, idx |
    if idx > 0
        if val > file_data[idx - 1]
        d += 1
        end
    end
end

puts "First solution:", d

d = 0
file_data.each_with_index do | val, idx |
    if idx <= (file_data.length - 4)
        if val < file_data[idx + 3]
            d += 1
        end
    else
        break
    end
end

puts "Second solution:", d