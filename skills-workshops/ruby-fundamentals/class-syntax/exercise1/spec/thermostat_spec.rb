require 'thermostat'

RSpec.describe Thermostat do
  it 'reports its current target temperature' do
    thermostat = Thermostat.new

    expect(thermostat.target_temperature).to eq(0)
  end

  it 'can increase' do
    thermostat = Thermostat.new

    thermostat.increase(10)

    expect(thermostat.target_temperature).to eq(10)
  end

  it 'can decrease' do
    thermostat = Thermostat.new
    thermostat.increase(20)

    thermostat.decrease(5)

    expect(thermostat.target_temperature).to eq(15)
  end
end
