package com.reservationapp.test;

import com.reservationapp.model.Reservation;
import com.reservationapp.service.ReservationService;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.web.client.TestRestTemplate;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;

import java.time.LocalDate;
import java.time.LocalTime;
import java.util.List;

import static org.assertj.core.api.Assertions.assertThat;

@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
public class ReservationControllerTest {

    @Autowired
    private TestRestTemplate restTemplate;

    @Autowired
    private ReservationService reservationService;

    @Test
    public void testGetAllReservations() {
        ResponseEntity<List> response = restTemplate.getForEntity("/api/reservations", List.class);
        assertThat(response.getStatusCode()).isEqualTo(HttpStatus.OK);
    }

    @Test
    public void testBookReservation() {
        Reservation reservation = new Reservation("John Doe", LocalDate.now(), LocalTime.now());
        ResponseEntity<Reservation> response = restTemplate.postForEntity("/api/reservations/book", reservation, Reservation.class);
        assertThat(response.getStatusCode()).isEqualTo(HttpStatus.OK);
        assertThat(response.getBody()).isNotNull();
        assertThat(response.getBody().getCustomerName()).isEqualTo("John Doe");
    }

    @Test
    public void testCancelReservation() {
        Reservation reservation = new Reservation("Jane Doe", LocalDate.now(), LocalTime.now());
        Reservation savedReservation = reservationService.bookReservation(reservation);
        restTemplate.delete("/api/reservations/cancel/" + savedReservation.getId());
        assertThat(reservationService.getAllReservations()).doesNotContain(savedReservation);
    }
}
