import os

def generate_invitations(template, attendees):
    # Check Input Types
    if not isinstance(template, str):
        print("Error: Template is not a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print("Error: Attendees is not a list of dictionaries.")
        return

    # Handle Empty Inputs
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process Each Attendee
    for index, attendee in enumerate(attendees, start=1):
        try:
            # Replace placeholders with values or "N/A" if missing
            content = template
            content = content.replace("{name}", attendee.get("name") or "N/A")
            content = content.replace("{event_title}", attendee.get("event_title") or "N/A")
            content = content.replace("{event_date}", attendee.get("event_date") or "N/A")
            content = content.replace("{event_location}", attendee.get("event_location") or "N/A")

            # Generate Output File
            output_filename = f"output_{index}.txt"
            
            # Write to file
            if os.path.exists(output_filename):
                continue # Or overwrite, but usually safer to check
            
            with open(output_filename, 'w') as f:
                f.write(content)
        except Exception as e:
            print(f"An error occurred processing attendee {index}: {e}")
