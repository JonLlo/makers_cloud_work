class Apprentice

  def initialize(first_name, last_name, program, employer)
    @first_name = first_name
    @last_name = last_name
    @program = program
    @employer = employer
  end

  def first_name
    @first_name
  end

  def last_name
    @last_name
  end

  def program
    @program
  end

  def employer
    @employer
  end

  def summary
    "#{full_name}, #{program} – #{employer}"
  end
end
