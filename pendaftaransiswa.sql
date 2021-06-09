-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 09 Jun 2021 pada 14.53
-- Versi server: 10.4.17-MariaDB
-- Versi PHP: 8.0.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `pendaftaransiswa`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `admin`
--

CREATE TABLE `admin` (
  `id` int(20) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `admin`
--

INSERT INTO `admin` (`id`, `username`, `password`) VALUES
(1, 'Admin', 'Admin');

-- --------------------------------------------------------

--
-- Struktur dari tabel `akunsiswa`
--

CREATE TABLE `akunsiswa` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `akunsiswa`
--

INSERT INTO `akunsiswa` (`id`, `username`, `password`) VALUES
(1, 'Siswa', 'Siswa'),
(2, 'Rio', 'Rio123');

-- --------------------------------------------------------

--
-- Struktur dari tabel `siswa`
--

CREATE TABLE `siswa` (
  `id` int(11) NOT NULL,
  `Username` varchar(50) NOT NULL,
  `Password` varchar(50) NOT NULL,
  `Nama` varchar(50) NOT NULL,
  `Tgl` varchar(255) NOT NULL,
  `NIK` varchar(50) NOT NULL,
  `Notelp` varchar(50) NOT NULL,
  `Agama` varchar(50) NOT NULL,
  `Jenis` varchar(50) NOT NULL,
  `Alamat` varchar(50) NOT NULL,
  `Ayah` varchar(50) NOT NULL,
  `PekerjaanAyah` varchar(50) NOT NULL,
  `PenghasilanAyah` varchar(50) NOT NULL,
  `Ibu` varchar(50) NOT NULL,
  `PekerjaanIbu` varchar(50) NOT NULL,
  `PenghasilanIbu` varchar(50) NOT NULL,
  `NoTelpOrtu` varchar(50) NOT NULL,
  `AlamatOrtu` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `siswa`
--

INSERT INTO `siswa` (`id`, `Username`, `Password`, `Nama`, `Tgl`, `NIK`, `Notelp`, `Agama`, `Jenis`, `Alamat`, `Ayah`, `PekerjaanAyah`, `PenghasilanAyah`, `Ibu`, `PekerjaanIbu`, `PenghasilanIbu`, `NoTelpOrtu`, `AlamatOrtu`) VALUES
(1, 'rio123', 'rio12', 'Rio', '25-1-2000', '123456789', '0987654321', 'Islam', 'Pria', 'Jl.Raya 1', 'Usep', 'PNS', '1.000.000', 'Lia', 'PNS', '1.000.000', '0987654321', 'Jl.Raya 1'),
(23, 'Sania00', 'San00', 'cehdc', 'nnncnd', 'odcodc', 'kncoodweocb', 'BUDHA', 'PRIA', 'cnopdhccdhd', 'pjcodoc', 'SWASTA', '> 3.000.000', 'fjowjhfer', 'PNS', '1.500.000 - 3.000.000', 'fjog0wh', 'oehfpowe');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `admin`
--
ALTER TABLE `admin`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `akunsiswa`
--
ALTER TABLE `akunsiswa`
  ADD PRIMARY KEY (`id`);

--
-- Indeks untuk tabel `siswa`
--
ALTER TABLE `siswa`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `admin`
--
ALTER TABLE `admin`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT untuk tabel `akunsiswa`
--
ALTER TABLE `akunsiswa`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT untuk tabel `siswa`
--
ALTER TABLE `siswa`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
