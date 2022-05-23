aviocompany_name=str(input())
adult_tickets_count=int(input())
children_tickets_count=int(input())
adult_ticket_cost=float(input())
service_price=float(input())
children_ticket_cost_1=0.3*adult_ticket_cost
adult_ticket_cost_final=adult_ticket_cost+service_price
children_ticket_cost_final=children_ticket_cost_1+service_price
sum_costs=0.2*(children_tickets_count*children_ticket_cost_final+adult_tickets_count*adult_ticket_cost_final)
print(f'The profit of your agency from {aviocompany_name} tickets is {format(sum_costs, ".2f")} lv.')
