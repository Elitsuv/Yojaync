from database import create_event_table, insert_event, get_all_events

def create_event(name, date, time, location, description):
    """Creates a new event in the database."""
    insert_event(name, date, time, location, description)
    print(f"Event '{name}' created successfully!")

def view_events():
    """Displays all events from the database."""
    events = get_all_events()
    if events:
        print("\nUpcoming Events:")
        for event in events:
            print(f"Name: {event[1]}")
            print(f"Date: {event[2]}")
            print(f"Time: {event[3]}")
            print(f"Location: {event[4]}")
            print(f"Description: {event[5]}")
            print("-" * 20)
    else:
        print("No upcoming events found.")

def main():
    
    create_event_table()
    
    while True:
        print("\nCommunity Event Manager")
        print("1. Create Event")
        print("2. View Events")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            
            name = input("Enter event name: ")
            date = input("Enter event date (YYYY-MM-DD): ")
            time = input("Enter event time (HH:MM): ")
            location = input("Enter event location: ")
            description = input("Enter event description: ")
            
            create_event(name, date, time, location, description)
        elif choice == '2':
            
            view_events()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
