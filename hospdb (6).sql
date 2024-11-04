-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 20, 2024 at 08:15 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

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
-- Table structure for table `addmedicinetb`
--

CREATE TABLE `addmedicinetb` (
  `id` int(11) NOT NULL,
  `category` varchar(40) NOT NULL,
  `medicine` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `addmedicinetb`
--

INSERT INTO `addmedicinetb` (`id`, `category`, `medicine`) VALUES
(21, 'tablets', 'parecetomol'),
(22, 'tablets', 'antibiotics'),
(23, 'tablets', 'aspirin'),
(24, 'tablets', 'atorvastin');

-- --------------------------------------------------------

--
-- Table structure for table `doctorprescriptiontb`
--

CREATE TABLE `doctorprescriptiontb` (
  `id` int(11) NOT NULL,
  `category` varchar(40) NOT NULL,
  `medicine` varchar(40) NOT NULL,
  `quantity` varchar(40) NOT NULL,
  `time` varchar(40) NOT NULL,
  `patientusername` varchar(40) NOT NULL,
  `doctorusername` varchar(40) NOT NULL,
  `date` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `doctorprescriptiontb`
--

INSERT INTO `doctorprescriptiontb` (`id`, `category`, `medicine`, `quantity`, `time`, `patientusername`, `doctorusername`, `date`) VALUES
(1, 'tablets', 'antibiotics', '10', '1-1-1', 'm4304', 'davis', '2024-10-20'),
(2, 'tablets', 'parecetomol', '1', '1-0-1', 'jw1234', 'alexa', '2024-10-20'),
(3, 'tablets', 'parecetomol', '5', '1-1-1', 'rm123', 'alexa', '2024-10-20');

-- --------------------------------------------------------

--
-- Table structure for table `logtb`
--

CREATE TABLE `logtb` (
  `id` int(11) NOT NULL,
  `username` varchar(40) NOT NULL,
  `password` varchar(40) NOT NULL,
  `type` varchar(40) NOT NULL,
  `status` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `logtb`
--

INSERT INTO `logtb` (`id`, `username`, `password`, `type`, `status`) VALUES
(1, 'admin', '123', 'admin', '1'),
(2, 'edward', '123', 'hr', '1'),
(6, 'alex', '123', 'doctor', '1'),
(8, 'roman', '123', 'pharmacist', '1'),
(10, 'Jack', '123', 'receptionist', '1'),
(16, 'alexa', '123', 'doctor', '1'),
(17, 'davis', '123', 'doctor', '1'),
(28, 's', '123', 'medicalsupredent', '1'),
(29, 'm1787', '123', 'patient', '0'),
(30, 'm4304', '123', 'patient', '0'),
(31, 'jw1234', '123', 'patient', '0'),
(32, 'rm123', '123', 'patient', '0'),
(33, 'mn123', '123', 'doctor', '1');

-- --------------------------------------------------------

--
-- Table structure for table `managedeptb`
--

CREATE TABLE `managedeptb` (
  `id` int(11) NOT NULL,
  `managedepartment` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `managedeptb`
--

INSERT INTO `managedeptb` (`id`, `managedepartment`) VALUES
(2, 'General Medicine'),
(4, 'dermatology'),
(6, 'cardiology'),
(7, 'ophthalmology'),
(8, 'pediatric');

-- --------------------------------------------------------

--
-- Table structure for table `managedoctortb`
--

CREATE TABLE `managedoctortb` (
  `id` int(11) NOT NULL,
  `name` varchar(40) NOT NULL,
  `address` varchar(40) NOT NULL,
  `photo` varchar(40) NOT NULL,
  `number` varchar(40) NOT NULL,
  `email` varchar(40) NOT NULL,
  `username` varchar(40) NOT NULL,
  `password` varchar(40) NOT NULL,
  `age` varchar(40) NOT NULL,
  `qualification` varchar(40) NOT NULL,
  `experience` varchar(40) NOT NULL,
  `speciality` varchar(40) NOT NULL,
  `typesof` varchar(40) NOT NULL,
  `biography` varchar(40) NOT NULL,
  `department` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `managedoctortb`
--

INSERT INTO `managedoctortb` (`id`, `name`, `address`, `photo`, `number`, `email`, `username`, `password`, `age`, `qualification`, `experience`, `speciality`, `typesof`, `biography`, `department`) VALUES
(1, 'Alex', ' savior-villa', 'hosp doctor.jpeg', '9568958657', 'alex@gmail.com', 'alex', '123', '40', 'Mbbs', '20+ Years', 'Ortho', 'Fulltime', ' Well Experienced', ''),
(6, 'alexa', ' tvm', 'hosp doctor.jpeg', '9567526585', 'alexa@gmail.com', 'alexa', '123', '25', 'mbbs', '5', 'full', 'fulltime', ' good', 'General Medicine'),
(7, 'davis', ' tvm', 'hosp doctor.jpeg', '9858985875', 'davis@gmail.com', 'davis', '123', '25', 'mbbs', '5', '5', '5', ' 5', 'cardiology'),
(9, 'manu', ' tvm', 'msd 2018 ipl.jpg', '9858985478', 'manu@gmail.com', 'mn123', '123', '25', 'F', 'd', 'd', 'full-time', ' d', 'Choose Department');

-- --------------------------------------------------------

--
-- Table structure for table `managehrtb`
--

CREATE TABLE `managehrtb` (
  `id` int(11) NOT NULL,
  `name` varchar(40) NOT NULL,
  `address` varchar(40) NOT NULL,
  `photo` varchar(40) NOT NULL,
  `number` varchar(40) NOT NULL,
  `email` varchar(40) NOT NULL,
  `username` varchar(40) NOT NULL,
  `password` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `managehrtb`
--

INSERT INTO `managehrtb` (`id`, `name`, `address`, `photo`, `number`, `email`, `username`, `password`) VALUES
(1, 'Edward', ' Fort-villa', 'hosp hr.jpeg', '945652255', 'edward@gmail.com', 'edward', '123');

-- --------------------------------------------------------

--
-- Table structure for table `managemedical`
--

CREATE TABLE `managemedical` (
  `id` int(11) NOT NULL,
  `name` varchar(40) NOT NULL,
  `address` varchar(40) NOT NULL,
  `photo` varchar(40) NOT NULL,
  `number` varchar(40) NOT NULL,
  `email` varchar(40) NOT NULL,
  `username` varchar(40) NOT NULL,
  `password` varchar(40) NOT NULL,
  `age` varchar(40) NOT NULL,
  `qualification` varchar(40) NOT NULL,
  `experience` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `managemedical`
--

INSERT INTO `managemedical` (`id`, `name`, `address`, `photo`, `number`, `email`, `username`, `password`, `age`, `qualification`, `experience`) VALUES
(3, 'sb', '  s', '44e10b16e649b691 flip2.webp', '77', 'mahi@mm', 's', '123', '50', 'd', 'd');

-- --------------------------------------------------------

--
-- Table structure for table `managepatienttb`
--

CREATE TABLE `managepatienttb` (
  `id` int(11) NOT NULL,
  `name` varchar(40) NOT NULL,
  `address` varchar(40) NOT NULL,
  `number` varchar(40) NOT NULL,
  `email` varchar(40) NOT NULL,
  `username` varchar(40) NOT NULL,
  `password` varchar(40) NOT NULL,
  `age` varchar(40) NOT NULL,
  `receptionusername` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `managepatienttb`
--

INSERT INTO `managepatienttb` (`id`, `name`, `address`, `number`, `email`, `username`, `password`, `age`, `receptionusername`) VALUES
(10, 'Nisham', ' tvm', '9656854751', 'nisham@gmail.com', 'm4304', '123', '31', 'jack'),
(11, 'jewel s  Dabilu', '  kollam,chathannur', '8281879675', 'jewel.s.dabilu12@gmail.com', 'jw1234', '123', '23', 'jack'),
(12, 'ram', ' tvm', '989648754', 'ram@gmail.com', 'rm123', '123', '25', 'jack');

-- --------------------------------------------------------

--
-- Table structure for table `managepharmacytb`
--

CREATE TABLE `managepharmacytb` (
  `id` int(11) NOT NULL,
  `name` varchar(40) NOT NULL,
  `address` varchar(40) NOT NULL,
  `photo` varchar(40) NOT NULL,
  `number` varchar(40) NOT NULL,
  `email` varchar(40) NOT NULL,
  `username` varchar(40) NOT NULL,
  `password` varchar(40) NOT NULL,
  `age` varchar(40) NOT NULL,
  `qualification` varchar(40) NOT NULL,
  `experience` varchar(40) NOT NULL,
  `biography` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `managepharmacytb`
--

INSERT INTO `managepharmacytb` (`id`, `name`, `address`, `photo`, `number`, `email`, `username`, `password`, `age`, `qualification`, `experience`, `biography`) VALUES
(1, 'Roman', ' Villa-coltan ', 'hosp pharmacist.avif', '9558654577', 'roman@gmail.com', 'roman', '123', '40', 'Mbbs', '20+ Years', ' Experienced ');

-- --------------------------------------------------------

--
-- Table structure for table `managereceptiontb`
--

CREATE TABLE `managereceptiontb` (
  `id` int(11) NOT NULL,
  `name` varchar(40) NOT NULL,
  `address` varchar(40) NOT NULL,
  `photo` varchar(40) NOT NULL,
  `number` varchar(40) NOT NULL,
  `email` varchar(40) NOT NULL,
  `username` varchar(40) NOT NULL,
  `password` varchar(40) NOT NULL,
  `age` varchar(40) NOT NULL,
  `qualification` varchar(40) NOT NULL,
  `experience` varchar(40) NOT NULL,
  `biography` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `managereceptiontb`
--

INSERT INTO `managereceptiontb` (`id`, `name`, `address`, `photo`, `number`, `email`, `username`, `password`, `age`, `qualification`, `experience`, `biography`) VALUES
(1, 'Jack kallis', ' Southern-fort ', 'hosp reception.jpg', '945652357', 'jack@gmail.com', 'Jack', '123', '35', 'Mbbs', '10+ Years', ' Experienced ');

-- --------------------------------------------------------

--
-- Table structure for table `patientcomplainttb`
--

CREATE TABLE `patientcomplainttb` (
  `id` int(11) NOT NULL,
  `complaint` varchar(40) NOT NULL,
  `date` varchar(40) NOT NULL,
  `patientusername` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `patientcomplainttb`
--

INSERT INTO `patientcomplainttb` (`id`, `complaint`, `date`, `patientusername`) VALUES
(12, ' doctor behaviour is bad', '2024-10-20', 'm4304'),
(13, ' could have improved', '2024-10-20', 'jw1234');

-- --------------------------------------------------------

--
-- Table structure for table `patientconsultationtb`
--

CREATE TABLE `patientconsultationtb` (
  `id` int(11) NOT NULL,
  `name` varchar(40) NOT NULL,
  `department` varchar(40) NOT NULL,
  `doctor` varchar(40) NOT NULL,
  `date` varchar(40) NOT NULL,
  `status` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `patientconsultationtb`
--

INSERT INTO `patientconsultationtb` (`id`, `name`, `department`, `doctor`, `date`, `status`) VALUES
(32, 'm4304', 'cardiology', 'davis', '2024-10-20', '1'),
(33, 'jw1234', 'General Medicine', 'alexa', '2024-10-20', '1'),
(34, 'rm123', 'General Medicine', 'alexa', '2024-10-20', '1');

-- --------------------------------------------------------

--
-- Table structure for table `patientobservationtb`
--

CREATE TABLE `patientobservationtb` (
  `id` int(11) NOT NULL,
  `height` varchar(40) NOT NULL,
  `weight` varchar(40) NOT NULL,
  `bp` varchar(40) NOT NULL,
  `temperature` varchar(40) NOT NULL,
  `observation` varchar(40) NOT NULL,
  `patientusername` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `patientobservationtb`
--

INSERT INTO `patientobservationtb` (`id`, `height`, `weight`, `bp`, `temperature`, `observation`, `patientusername`) VALUES
(16, '177 cm', '80 kg', '80-120', '100 deg', ' chest pain', 'm4304'),
(17, '160 cm', '62 kg', '80-120', '80 deg', ' cough,fever, severe cold', 'jw1234'),
(18, '177 cm', '65 kg', '80-120', '100 deg', ' fever', 'rm123');

-- --------------------------------------------------------

--
-- Table structure for table `pharmacybilling`
--

CREATE TABLE `pharmacybilling` (
  `medicine` varchar(40) NOT NULL,
  `quantity` varchar(40) NOT NULL,
  `time` varchar(40) NOT NULL,
  `pharmacyusername` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `pharmacybillingaddtb`
--

INSERT INTO `pharmacybillingaddtb` (`id`, `prescriptionid`, `pharmacyusername`, `medicine`, `date`, `patientusername`, `quantity`, `status`, `billno`) VALUES
(38, '1', 'roman', 'antibiotics', '2024-10-20', 'm4304', '10', '1', '100'),
(39, '2', 'roman', 'parecetomol', '2024-10-20', 'jw1234', '1', '1', '101'),
(40, '3', 'roman', 'parecetomol', '2024-10-20', 'rm123', '5', '1', '102');

-- --------------------------------------------------------

--
-- Table structure for table `pharmacyfinishtb`
--

CREATE TABLE `pharmacyfinishtb` (
  `id` int(11) NOT NULL,
  `billno` varchar(40) NOT NULL,
  `date` varchar(40) NOT NULL,
  `patients` varchar(40) NOT NULL,
  `pharmacist` varchar(40) NOT NULL,
  `total` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `pharmacyfinishtb`
--

INSERT INTO `pharmacyfinishtb` (`id`, `billno`, `date`, `patients`, `pharmacist`, `total`) VALUES
(6, '100', '2024-10-20', 'm4304', 'roman', '200.0'),
(7, '101', '2024-10-20', 'jw1234', 'roman', '10.0'),
(8, '102', '2024-10-20', 'rm123', 'roman', '50.0');

-- --------------------------------------------------------

--
-- Table structure for table `stockdtb`
--

CREATE TABLE `stockdtb` (
  `id` int(11) NOT NULL,
  `category` varchar(40) NOT NULL,
  `medicine` varchar(40) NOT NULL,
  `date` varchar(40) NOT NULL,
  `pharmacyusername` varchar(40) NOT NULL,
  `quantity` varchar(40) NOT NULL,
  `price` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `stockdtb`
--

INSERT INTO `stockdtb` (`id`, `category`, `medicine`, `date`, `pharmacyusername`, `quantity`, `price`) VALUES
(21, 'tablets', 'antibiotics', '2024-10-20', 'roman', '100', '20'),
(22, 'tablets', 'parecetomol', '2024-10-20', 'roman', '110', '10'),
(23, 'tablets', 'parecetomol', '2024-10-20', 'roman', '100', '10');

-- --------------------------------------------------------

--
-- Table structure for table `stockqtb`
--

CREATE TABLE `stockqtb` (
  `id` int(11) NOT NULL,
  `category` varchar(40) NOT NULL,
  `medicine` varchar(40) NOT NULL,
  `quantity` varchar(40) NOT NULL,
  `price` varchar(40) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `stockqtb`
--

INSERT INTO `stockqtb` (`id`, `category`, `medicine`, `quantity`, `price`) VALUES
(8, 'tablets', 'antibiotics', '80', '20'),
(9, 'tablets', 'parecetomol', '94', '10');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `addmedicinetb`
--
ALTER TABLE `addmedicinetb`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `doctorprescriptiontb`
--
ALTER TABLE `doctorprescriptiontb`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `logtb`
--
ALTER TABLE `logtb`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `managedeptb`
--
ALTER TABLE `managedeptb`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `managedoctortb`
--
ALTER TABLE `managedoctortb`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `managehrtb`
--
ALTER TABLE `managehrtb`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `managemedical`
--
ALTER TABLE `managemedical`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `managepatienttb`
--
ALTER TABLE `managepatienttb`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `managepharmacytb`
--
ALTER TABLE `managepharmacytb`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `managereceptiontb`
--
ALTER TABLE `managereceptiontb`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `patientcomplainttb`
--
ALTER TABLE `patientcomplainttb`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `patientconsultationtb`
--
ALTER TABLE `patientconsultationtb`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `patientobservationtb`
--
ALTER TABLE `patientobservationtb`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `pharmacybillingaddtb`
--
ALTER TABLE `pharmacybillingaddtb`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `pharmacyfinishtb`
--
ALTER TABLE `pharmacyfinishtb`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `stockdtb`
--
ALTER TABLE `stockdtb`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `stockqtb`
--
ALTER TABLE `stockqtb`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `addmedicinetb`
--
ALTER TABLE `addmedicinetb`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT for table `doctorprescriptiontb`
--
ALTER TABLE `doctorprescriptiontb`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `logtb`
--
ALTER TABLE `logtb`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

--
-- AUTO_INCREMENT for table `managedeptb`
--
ALTER TABLE `managedeptb`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `managedoctortb`
--
ALTER TABLE `managedoctortb`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT for table `managehrtb`
--
ALTER TABLE `managehrtb`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `managemedical`
--
ALTER TABLE `managemedical`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT for table `managepatienttb`
--
ALTER TABLE `managepatienttb`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `managepharmacytb`
--
ALTER TABLE `managepharmacytb`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `managereceptiontb`
--
ALTER TABLE `managereceptiontb`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `patientcomplainttb`
--
ALTER TABLE `patientcomplainttb`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `patientconsultationtb`
--
ALTER TABLE `patientconsultationtb`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;

--
-- AUTO_INCREMENT for table `patientobservationtb`
--
ALTER TABLE `patientobservationtb`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `pharmacybillingaddtb`
--
ALTER TABLE `pharmacybillingaddtb`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT for table `pharmacyfinishtb`
--
ALTER TABLE `pharmacyfinishtb`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `stockdtb`
--
ALTER TABLE `stockdtb`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `stockqtb`
--
ALTER TABLE `stockqtb`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
