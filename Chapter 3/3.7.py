invited_people = ['tata', 'mama', 'Rafał']
print(invited_people[0] + ", zapraszam Cię na obiad")
print(invited_people[1] + ", zapraszam Cię na obiad")
print(invited_people[2] + ", zapraszam Cię na obiad")

print("\n" + invited_people[2] + " nie może przyjść.")

invited_people[2] = "Babcia"
print("\n" + invited_people[0] + ", zapraszam Cię na obiad")
print(invited_people[1] + ", zapraszam Cię na obiad")
print(invited_people[2] + ", zapraszam Cię na obiad")

print("\nZnalazłem większy stół.")

invited_people.insert(0, 'Tomek')
invited_people.insert(2, 'Marcel')
invited_people.append('Romek')

print("\n" + invited_people[0] + ", zapraszam Cię na obiad")
print(invited_people[1] + ", zapraszam Cię na obiad")
print(invited_people[2] + ", zapraszam Cię na obiad")
print(invited_people[3] + ", zapraszam Cię na obiad")
print(invited_people[4] + ", zapraszam Cię na obiad")

print("\nmogę zaprosić jednak tylko 2 osoby")
popped_person = invited_people.pop()
print("\n" + popped_person + ", sorry ale wypad, nie ma miejsca")

popped_person2 = 'Marcel'
invited_people.remove(popped_person2)
print(popped_person2 + ", sorry ale wypad, nie ma miejsca")

popped_person = invited_people.pop()
print(popped_person + ", sorry ale wypad, nie ma miejsca")

popped_person2 = 'Tomek'
invited_people.remove(popped_person2)
print(popped_person2 + ", sorry ale wypad, nie ma miejsca")

print("\n" + invited_people[0] + ", wciąż zapraszam Cię na obiad")
print(invited_people[1] + ", wciąż zapraszam Cię na obiad")

del invited_people[0, 1]
print(invited_people)