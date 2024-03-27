class Car:
    def __init__(self, name, units_sold, satisfaction_rating):
        self.name = name
        self.units_sold = units_sold
        self.satisfaction_rating = satisfaction_rating


def total_cars_sold(cars):
    total_sold = sum(car.units_sold for car in cars)
    return total_sold


def most_popular_car_model(cars):
    max_sold = max(cars, key=lambda x: x.units_sold)
    return max_sold.name


def high_customer_satisfaction_models(cars):
    high_satisfaction_cars = [car.name for car in cars if car.satisfaction_rating > 4]
    return high_satisfaction_cars


def average_customer_satisfaction_score(cars):
    total_ratings = sum(car.satisfaction_rating for car in cars)
    average_score = total_ratings / len(cars)
    return average_score


def underperforming_models(cars):
    average_score = average_customer_satisfaction_score(cars)
    underperforming = [(car.name, car.units_sold, car.satisfaction_rating) for car in cars if car.units_sold < total_cars_sold(cars)/len(cars)]
    return underperforming


def main():
    # Create dataset for 20 car models
    product_names = ["Toyota Camry", "Honda Accord", "Ford Mustang", "Chevrolet Silverado", "Nissan Altima",
                     "BMW 3 Series", "Mercedes-Benz C-Class", "Audi A4", "Hyundai Sonata", "Kia Optima",
                     "Lexus ES", "Tesla Model 3", "Subaru Outback", "Ford Explorer", "Toyota RAV4",
                     "Jeep Wrangler", "GMC Sierra", "Volkswagen Jetta", "Mazda CX-5", "Volvo XC60"]

    units_sold = [150, 200, 100, 75, 250, 180, 220, 120, 160, 140,
                  190, 210, 170, 130, 240, 110, 230, 90, 170, 200]

    customer_reviews = [4.3, 4.5, 4.1, 4.6, 4.2, 4.4, 4.7, 4.8, 4.0, 4.2,
                        4.6, 4.9, 4.4, 4.3, 4.5, 4.1, 4.7, 4.3, 4.6, 4.5]

    cars = [Car(name, units_sold, satisfaction_rating) for name, units_sold, satisfaction_rating in zip(product_names, units_sold, customer_reviews)]

    # Answer the questions
    print("1. Total Cars Sold:", total_cars_sold(cars))
    print("2. Most Popular Car Model:", most_popular_car_model(cars))
    print("3. High Customer Satisfaction Models:", high_customer_satisfaction_models(cars))
    print("4. Average Customer Satisfaction Score:", average_customer_satisfaction_score(cars))
    print("5. Underperforming Models:")
    underperforming = underperforming_models(cars)
    for model in underperforming:
        print("- Name:", model[0], "| Units Sold:", model[1], "| Satisfaction Rating:", model[2])


if __name__ == "__main__":
    main()
