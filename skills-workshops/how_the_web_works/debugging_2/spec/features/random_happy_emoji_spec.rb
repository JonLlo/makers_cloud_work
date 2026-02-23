require "capybara/rspec"
require_relative "../../lib/app"

Capybara.app = StruggleTableFlipperApp

feature "show a random happy emoji on the home page" do

  scenario "the home page returns a successful status code" do
    visit("/")
    expect(page.status_code).to eq(200)
  end

  scenario "a random happy emoji appears" do
    visit("/")
    expect(page).to have_content(':)').or have_content(':D')
  end

end
