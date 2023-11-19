### Recruitment Challenge

The aim of this challenge is to add features to an existing simplified meal ordering platform.

#### 1. **User Authentication:**
   - A client-side modal for login and registration.
   - New endpoints on the server side to handle login and registration.
   - Necessary database structures (i.e. a `User` table) and persist user data upon registration.
   - Re-directing user when they try to access routes without authentication.
   - Respective flash messages for registered and non-existing mail IDs.

#### 2. **Dish Orders:**
   - Users will be able to order dishes
      1. By first putting dishes into a shopping cart.
      2. And then submitting the content of the shopping cart as order to the server.
      3. The server persists that order in the database.

#### 3. **Dish Reviews:**
   - Users will be able to:
      1. Provide a rating for a dish from 1 to 5.
      2. Leave a comment alongside their rating.
      3. View the average rating of the dish.
      4. View comments and associated ratings of other users.
   - One user can only give one review per dish, and only after having ordered that dish.
   - Reviews (rating and comments) should be persisted in the database.

#### 4. **User-Restaurant Chat:**
   - Interactive chat feature between user and restaurant employee. The content of the employee's responses are hardcoded.
   - Allowing users to:
      1. Initiate and end chat conversations.
      2. The chat should automatically end if the customer is inactive for a predetermined period.

#### 5. **Order Page:**
   - Ensure users can only view their own order history.
   - Implement an order tracking feature that allows to view the status/progress of a user's orders.
   - An order can be in either of the following states:
      - **Submitted:** User submitted the order. Restaurant is reviewing.
      - **Approved:** Restaurant approved the order
      - **Rejected:** Restaurant rejected the order
      - **Canceled:** User canceled the order
      - **In Preparation:** Restaurant is preparing the order
      - **In Delivery:** The order is out for delivery
      - **Delivered:** The order has been delivered
   - A user can only cancel an order as long as the order is not yet in preparation.
