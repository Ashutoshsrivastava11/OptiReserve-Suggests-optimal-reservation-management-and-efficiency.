-- Drop existing triggers if they exist
DROP TRIGGER IF EXISTS update_reservation_status ON reservations;
DROP FUNCTION IF EXISTS update_reservation_status_func;

-- Create a function to update reservation status
CREATE OR REPLACE FUNCTION update_reservation_status_func()
RETURNS TRIGGER AS $$
BEGIN
    -- Automatically update the status based on custom logic
    IF NEW.reservation_date < CURRENT_DATE AND NEW.status = 'pending' THEN
        NEW.status := 'canceled';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Create a trigger to call the function before inserting or updating reservations
CREATE TRIGGER update_reservation_status
BEFORE INSERT OR UPDATE ON reservations
FOR EACH ROW
EXECUTE FUNCTION update_reservation_status_func();
