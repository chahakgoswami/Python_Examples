def max_number_of_families(n, reserved_seats):
    seat_availability = {}

    for row, seat_no in reserved_seats:
        if row not in seat_availability:
            seat_availability[row] = [True] * 3
        seats = seat_availability[row]

        if seat_no == 1 or seat_no == 10:
            continue
        if 2 <= seat_no <= 3:
            seats[0] = False
        elif 4 <= seat_no <= 5:
            seats[0] = False
            seats[1] = False
        elif 6 <= seat_no <= 7:
            seats[1] = False
            seats[2] = False
        elif 8 <= seat_no <= 9:
            seats[2] = False

    count = 0
    for seats_avail in seat_availability.values():
        if seats_avail[0] and seats_avail[2]:
            count += 2
        elif seats_avail[0] or seats_avail[1] or seats_avail[2]:
            count += 1

    return count + 2 * (n - len(seat_availability))
