def kClosest(points, k):

    closests = []
    distances = {}

    for point in points:
        [x, y] = point
        distance = ( (x - 0)**2 + (y - 0)**2 ) ** 0.5

        values = distances.get(distance, [])
        values.append(point)
        distances[distance] = values
        
    list_of_distances = sorted(list(distances.keys()))

    for distance in list_of_distances:
        closests += distances[distance]

    return closests[:k]


    