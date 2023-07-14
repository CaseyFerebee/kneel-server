ORDERS = [
    {
        "metalsId": 1,
        "styleId": 2,
        "sizesId": 3,
        "id": 1
    },
    {
        "metalsId": 1,
        "styleId": 1,
        "sizesId": 1,
        "id": 2
    },
    {
        "metalsId": 1,
        "styleId": 1,
        "sizesId": 1,
        "id": 3
    },
    {
        "metalsId": 4,
        "styleId": 1,
        "sizesId": 2,
        "id": 4
    },
    {
        "metalsId": 5,
        "styleId": 1,
        "sizesId": 3,
        "id": 5
    },
    {
        "metalsId": 2,
        "styleId": 2,
        "sizesId": 1,
        "id": 6
    },
    {
        "metalsId": 1,
        "styleId": 1,
        "sizesId": 1,
        "id": 7
    },
    {
        "metalsId": 1,
        "styleId": 1,
        "sizesId": 1,
        "id": 8
    }
]


def get_all_orders():
    return ORDERS


def get_single_order(id):
    # Variable to hold the found animal, if it exists
    requested_order = None

    for order in ORDERS:

        if order["id"] == id:
            requested_order = order

    return requested_order


def create_order(order):
    # Get the id value of the last animal in the list
    max_id = ORDERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    order["id"] = new_id

    # Add the animal dictionary to the list
    ORDERS.append(order)

    # Return the dictionary with `id` property added
    return order


def delete_order(id):
    # Initial -1 value for animal index, in case one isn't found
    order_index = -1

    # Iterate the ANIMALS list, but use enumerate() so that you
    # can access the index value of each item
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            # Found the animal. Store the current index.
            order_index = index

    # If the animal was found, use pop(int) to remove it from list
    if order_index >= 0:
        ORDERS.pop(order_index)


def update_order(id, new_order):
    # Iterate the ANIMALS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            # Found the animal. Update the value.
            ORDERS[index] = new_order
            break
