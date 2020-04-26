# VT Solutions Backend Testcase

## What was done

- Complete model definition for the system (models `User` (from existing Django model), `Hotel`, `RoomCategory`, `Room`, `Booking`)
- Views for each model (and more)
- Filtering `Hotel`, `RoomCategory`, `Room`, `Booking` based on their relation to user account
- All requested endpoints (except one, create `Booking` with overlapping control)
- Manual testing to check the correspondence to the requirements

## What was not done

- Did not test password change, it may not work
- Did not implement creating bookings (I could just add create view without overlapping check, but I decided not to)
- No filtering/searching for admin panel
- No Swagger documentation

## Endpoints Description 

- `HTTP GET admin/`: admin panel
- `HTTP POST (username, password) api-auth/login/`: log in user`
- `HTTP GET api-auth/logout/`: log out user

- `HTTP GET users/`: get the list of all users (admin only)
- `HTTP GET users/{id}/`: get detailed information about the user 
- `HTTP PUT (old_password, new_password) users/change_password/`: update user password
- `HTTP GET hotels/`: get the list of all hotels where the current user is admin (returns all hotels for admin user)
- `HTTP GET hotels/{id}/`: get detailed information about the hotel (will return an empty response for not related users)
- `HTTP GET room_categories/`: get the list of room categories in all user-related hotels (in all hotels for admin users)
- `HTTP GET room_categories/{id}/`: get detailed information about the room category (will return an empty response for not related users)
- `HTTP GET rooms/`: get the list of all rooms in all user-related hotels (in all hotels for admin users)
- `HTTP GET rooms?room_category=<room_category_id>`: get the list of all rooms of the specified category
- `HTTP GET rooms/{id}/`: get detailed information about the room (will return an empty response for not related users) 
- `HTTP GET bookings/`: get the list of bookings for all user-related hotels (for all hotels for admin users)
- `HTTP GET bookings?room=<room_id>`: get the list of bookings for the specified room
- `HTTP GET bookings/{id}/`: get detailed information about the booking (will return an empty response for not related users)
