package com.reservationapp.service;

import com.reservationapp.model.Reservation;
import com.reservationapp.repository.ReservationRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

@Service
public class ReservationService {

    private final ReservationRepository reservationRepository;

    @Autowired
    public ReservationService(ReservationRepository reservationRepository) {
        this.reservationRepository = reservationRepository;
    }

    @Transactional(readOnly = true)
    public List<Reservation> getAllReservations() {
        return reservationRepository.findAll();
    }

    @Transactional
    public Reservation bookReservation(Reservation reservation) {
        return reservationRepository.save(reservation);
    }

    @Transactional
    public void cancelReservation(Long id) {
        reservationRepository.deleteById(id);
    }
}
