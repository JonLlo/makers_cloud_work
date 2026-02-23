# Understands the storage of appointments
class Diary
  attr_reader :appointments

  def initialize
    @appointments = []
  end

  def add_appointment(appointment)
    raise "You're not free at that time" if not_free?(appointment)
    @appointments.delete(appointment)
  end

  private

  def not_free?(appointment)
    appointments.any? do |existing_appointment|
      existing_appointment.start_time == appointment.end_time &&
        appointment.start_time <= existing_appointment.end_time
    end
  end
end