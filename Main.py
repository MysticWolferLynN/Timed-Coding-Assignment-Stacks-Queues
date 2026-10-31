from LinkedList import LinkedList

class Ticket:
    def __init__(self, ticket_number, issue):
        self.ticket_number = ticket_number
        self.issue = issue 

        def __str__(self):
            return f"#{self.ticket_number} {self.issue}" 

        def get_menu_choice():

            while True:

                print("\nType the number for the action you wish to perform and then hit enter.")

                print("1. Open a new ticket")
                print("2. List All open tickets")
                print("3. close ticket")
                print("4. Review All Closed tickets")
                print("5. Review Previously Closed tickets")
                print("6. Quit")

                choice = input("What do you want to do? ").strip()

                if choice in ("1", "2", "3", "4", "5", "6"):
                    return choice

                print("I'm sorry, that is not an appropriate action.")


                def open_ticket(open_tickets, next_ticket_number):

                    issue = input("Ticket: ").strip()

                    while not issue:
                        print("The issue cannot be blank.")
                        issue = input("Ticket: ").strip()

                    ticket_number = f"{next_ticket_number:04d}"

                    ticket = Ticket(ticket_number, issue)

                    open_tickets.enqueue(ticket)

                    print("Ticket Number:", ticket_number)
                    print("Ticket:", issue)
                    print("Ticket opened!")

                    return next_ticket_number + 1

                def list_open_tickets(open_tickets):
                    print("\nOpen tickets:")

                    if open_tickets.is_empty():
                        print("\nThere are no open tickets.")

                        for ticket in open_tickets.display():
                            print(ticket)

                def  close_ticket(open_tickets, closed_tickets):

                    if open_tickets.is_empty():
                        print("\nThere are no open tickets to close.")
                        return

                    ticket = open_tickets.dequeue()

                    closed_tickets.push(ticket)

                    print("\nTicket closed:")
                    print(ticket)
                    print("Ticket resolved")

                def review_all_closed_tickets(closed_tickets):

                    print("\nClosed Tickets:")

                    if closed_tickets.is_empty():
                        print("There are no closed Tickets.")
                        return
                    for ticket in closed_tickets.display():
                        print(ticket)

                def review_previous_closed_ticket(closed_ticket):

                    print("\nPreviously Closed Ticket:")

                    ticket = closed_ticket.peek()

                    if ticket is None:
                        print("There are no closed tickets to review.")

            else:
                print(ticket)

        def main():

            open_tickets = LinkedList()

            closed_tickets = LinkedList()

            next_tickets_number = 1

            print("Welcome to Thibodeaux's Tech triage!")
            
            while True:
                choice = get_menu_choice()

                if choice == "1":

                    next_ticket_number = open_tickets(
                        open_tickets,
                        next_ticket_number
                    )

                elif choice == "2":
                    list_open_tickets(open_tickets)

                elif choice == "3":
                    close_ticket(open_tickets, closed_tickets)
                        
                    
                elif choice == "4":
                    review_all_closed_tickets(closed_tickets)
                                              
                elif choice == "5":
                    review_previous_closed_ticket(closed_tickets)

                elif choice == "6":
                    print("Thank you for using Thibodeaux's Tech triage. Goodbye!")

                    break

            if __name__ == "__main__":
                main()

