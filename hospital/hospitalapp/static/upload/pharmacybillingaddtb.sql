-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 16, 2024 at 09:27 AM
-- Server version: 10.4.25-MariaDB
-- PHP Version: 8.1.10

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hospdb`
--

-- --------------------------------------------------------

--
-- Table structure for table `pharmacybillingaddtb`
--

CREATE TABLE `pharmacybillingaddtb` (
  `id` int(11) NOT NULL,
  `prescriptionid` varchar(40) NOT NULL,
  `pharmacyusername` varchar(40) NOT NULL,
  `medicine` varchar(40) NOT NULL,
  `date` varchar(40) NOT NULL,
  `patientusername` varchar(40) NOT NULL,
  `quantity` varchar(40) NOT NULL,
  `status` varchar(40) NOT NULL,
  `billno` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `pharmacybillingaddtb`
--

INSERT INTO `pharmacybillingaddtb` (`id`, `prescriptionid`, `pharmacyusername`, `medicine`, `date`, `patientusername`, `quantity`, `status`, `billno`) VALUES
(9, '52', 'roman', 'antibiotics', '2024-10-08', 'asfan', '10', '', ''),
(10, '51', 'roman', 'antibiotics', '2024-10-08', 'asfan', '100 mg', '', ''),
(11, '52', 'roman', 'antibiotics', '2024-10-10', 'asfan', '10', '', ''),
(14, '25', 'roman', 'paracetomol', '2024-10-10', 'asfan', '20', '', ''),
(15, '25', 'roman', 'parecetomol', '2024-10-10', 'asfan', '500 mg', '', ''),
(16, '53', 'roman', 'antibiotics', '2024-10-10', 'asfan', '40', '', ''),
(17, '54', 'roman', 'antibiotics', '2024-10-10', 'asfan', '20', '', ''),
(23, '56', 'roman', 'paracetomol', '2024-10-15', 'asfan', '10', '0', '0'),
(24, '56', 'roman', 'paracetomol', '2024-10-15', 'asfan', '10', '0', '0'),
(25, '56', 'roman', 'paracetomol', '2024-10-16', 'asfan', '10', '1', '100');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `pharmacybillingaddtb`
--
ALTER TABLE `pharmacybillingaddtb`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `pharmacybillingaddtb`
--
ALTER TABLE `pharmacybillingaddtb`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
