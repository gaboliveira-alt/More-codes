class Hotel:
    def __init__(self):
        self.rooms = {
            101: "available",
            102: "available",
            103: "available",
        }
    
    def check_in(self, room_number):
           if self.rooms[room_number] == "available":
               self.rooms[room_number] = "occupied"
           else:
               raise ValueError("RoomOccupiedError")
    
    def check_out(self, room_number):
        if self.rooms[room_number] == "occupied":
            self.rooms[room_number] = "available"
        else:
            raise ValueError("RoomAvailableError")
    
    def show_status(self):
        print(f'{self.rooms}')


def main():
    tech_hotel = Hotel()
    tech_hotel.check_in(101)
    tech_hotel.show_status()
    
    tech_hotel.check_in(103)
    tech_hotel.show_status()

if __name__ == '__main__':
    main()