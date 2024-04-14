from payscale import PyScale

pay_scale = PyScale()
pay_scale.go_to_site()

while True:
    # Get the data
    page_data, payscale2018 = pay_scale.get_data()

    # Check whether the button is active
    href = pay_scale.is_the_next_button_active()

    # If active, go to the next page
    if href:
        pay_scale.next_page()
    else:
        break

# Save data to CSV
csv_file_path = "./payscale_data_2018.csv"
pay_scale.save_data_to_csv(csv_file_path)

# Close the driver
pay_scale.close_driver()