def hot_dogs_required(guests):
    dogs_in_a_pack = 10
    num_guests = guests

    needed = num_guests // dogs_in_a_pack
    return needed


def hot_dogs_left_over(guests):
    dogs_in_a_pack = 10
    num_guests = guests

    left_over = num_guests % dogs_in_a_pack
    return left_over


def buns_required(guests):
    buns_in_a_pack = 8
    num_guests = guests

    needed = num_guests // buns_in_a_pack
    return needed


def buns_left_over(guests):
    buns_in_a_pack = 8
    num_guests = guests

    left_over = num_guests % buns_in_a_pack
    return left_over


guest_count = int(input("How many people will be attending your cookout? "))

print(f'For everyone to have at least one hot dog, you will need a minimum of {hot_dogs_required(guest_count)} packs '
      f'of hot dogs and you will have {hot_dogs_left_over(guest_count)} hot dogs left over.')

print(f'For everyone to have a bun for their hot dog, you will need a minimum of {buns_required(guest_count)} packs '
      f'of buns and you will have {buns_left_over(guest_count)} buns left over.')
