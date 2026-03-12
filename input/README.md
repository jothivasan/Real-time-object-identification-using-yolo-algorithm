# Input Images for YOLO Object Detection

This folder contains 20 sample images for testing the YOLO object detection system.

## Image List

| # | Filename | Objects to Detect |
|---|----------|-------------------|
| 1 | input_01_person_laptop.png | Person, Laptop, Mouse, Keyboard, Cup |
| 2 | input_02_car_street.png | Car |
| 3 | input_03_dog_cat.png | Dog, Cat, Couch |
| 4 | input_04_bicycle_park.png | Person, Bicycle |
| 5 | input_05_dining_table.png | Dining table, Pizza, Bottle, Cup |
| 6 | input_06_phone_backpack.png | Person, Cell phone, Backpack |
| 7 | input_07_bus_truck.png | Bus, Truck |
| 8 | input_08_tennis_player.png | Person, Tennis racket |
| 9 | input_09_living_room.png | TV, Couch, Chair, Potted plant |
| 10 | input_10_kitchen_items.png | Microwave, Bowl, Banana, Apple |
| 11 | input_11_skateboard.png | Person, Skateboard |
| 12 | input_12_airplane.png | Airplane |
| 13 | input_13_farm_animals.png | Horse, Sheep |
| 14 | input_14_bedroom.png | Bed, Clock, Book |
| 15 | input_15_surfing.png | Person, Surfboard |
| 16 | input_16_train_station.png | Train, Person |
| 17 | input_17_bird_elephant.png | Bird, Elephant |
| 18 | input_18_motorcycle.png | Motorcycle, Bicycle |
| 19 | input_19_baseball.png | Person, Baseball bat |
| 20 | input_20_boat_bear.png | Boat, Bear |

## Usage

These images can be used to:
- Test the YOLO object detection accuracy
- Demonstrate the web application functionality
- Benchmark detection performance
- Validate the model's capabilities across different object classes

## How to Use

1. Start the application: `python app.py`
2. Open the web interface at `http://localhost:5000`
3. Upload any of these images from the `input/` folder
4. Adjust confidence threshold as needed (recommended: 50%)
5. View the detection results

## Object Classes Covered

These 20 images cover a diverse range of the 80 COCO classes:
- **People & Activities**: Person, sports activities
- **Vehicles**: Car, Bus, Truck, Motorcycle, Bicycle, Airplane, Train, Boat
- **Animals**: Dog, Cat, Horse, Sheep, Bird, Elephant, Bear
- **Indoor Objects**: Laptop, TV, Couch, Chair, Bed, Dining table
- **Electronics**: Cell phone, Mouse, Keyboard, Microwave
- **Sports Equipment**: Tennis racket, Skateboard, Surfboard, Baseball bat
- **Food**: Pizza, Banana, Apple
- **Accessories**: Backpack, Cup, Bottle, Clock, Book

Total: ~40+ different object classes represented across the 20 images!
