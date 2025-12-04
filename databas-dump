--
-- PostgreSQL database dump
--

\restrict TsVMCkeb8lNUpjBWkCpmQc4yyUILnd2pggsE1P6dF1apXZhY1rNlnQXHzidlUiD

-- Dumped from database version 17.6 (Postgres.app)
-- Dumped by pg_dump version 17.6 (Postgres.app)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET transaction_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: activites; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.activites (
    id integer NOT NULL,
    travel_id integer,
    resturant_name character varying,
    activites_type character varying(255),
    start_time timestamp without time zone,
    end_time timestamp without time zone
);


ALTER TABLE public.activites OWNER TO postgres;

--
-- Name: activites_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.activites_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.activites_id_seq OWNER TO postgres;

--
-- Name: activites_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.activites_id_seq OWNED BY public.activites.id;


--
-- Name: booking; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.booking (
    id integer NOT NULL,
    user_id integer,
    travel_id integer,
    hotel_id integer,
    payment_id integer,
    adults integer,
    kids integer
);


ALTER TABLE public.booking OWNER TO postgres;

--
-- Name: booking_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.booking_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.booking_id_seq OWNER TO postgres;

--
-- Name: booking_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.booking_id_seq OWNED BY public.booking.id;


--
-- Name: booking_x_room; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.booking_x_room (
    booking_id integer,
    room_id integer
);


ALTER TABLE public.booking_x_room OWNER TO postgres;

--
-- Name: hotel; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.hotel (
    id integer NOT NULL,
    reigon character varying(255),
    city character varying(255),
    country character varying(255),
    hotel_name character varying(255),
    guest_limit integer,
    available integer
);


ALTER TABLE public.hotel OWNER TO postgres;

--
-- Name: transport; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.transport (
    id integer NOT NULL,
    departure_time timestamp without time zone,
    departure_place character varying(255),
    arrival_time timestamp without time zone,
    arrival_place character varying(255),
    home_departure_time timestamp without time zone,
    home_departure_place character varying(255),
    home_arrival_time timestamp without time zone,
    home_arrival_place character varying(255),
    transport_during_travel character varying(255)
);


ALTER TABLE public.transport OWNER TO postgres;

--
-- Name: travel; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.travel (
    id integer NOT NULL,
    transport_id integer,
    start_date timestamp without time zone,
    end_date character varying(255),
    price character varying(255)
);


ALTER TABLE public.travel OWNER TO postgres;

--
-- Name: detaljerad_beskrivning_om_varje_resa; Type: VIEW; Schema: public; Owner: postgres
--

CREATE VIEW public.detaljerad_beskrivning_om_varje_resa AS
 SELECT t2.departure_time,
    t2.departure_place,
    t2.arrival_time,
    t2.arrival_place,
    t2.home_departure_time,
    t2.home_departure_place,
    t2.home_arrival_time,
    t2.home_arrival_place,
    t2.transport_during_travel,
    h.hotel_name,
    h.city,
    h.country,
    h.reigon,
    a.resturant_name,
    a.activites_type,
    t.price
   FROM ((((public.booking
     JOIN public.hotel h ON ((booking.hotel_id = h.id)))
     JOIN public.travel t ON ((t.id = booking.travel_id)))
     JOIN public.activites a ON ((booking.travel_id = a.travel_id)))
     JOIN public.transport t2 ON ((t2.id = t.transport_id)))
  ORDER BY t2.departure_time;


ALTER VIEW public.detaljerad_beskrivning_om_varje_resa OWNER TO postgres;

--
-- Name: hotel_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.hotel_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.hotel_id_seq OWNER TO postgres;

--
-- Name: hotel_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.hotel_id_seq OWNED BY public.hotel.id;


--
-- Name: payment; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.payment (
    id integer NOT NULL,
    payment_type character varying(255),
    payment_date date
);


ALTER TABLE public.payment OWNER TO postgres;

--
-- Name: user; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."user" (
    id integer NOT NULL,
    first_name character varying(255),
    last_name character varying(255),
    email character varying(255),
    password character varying(255)
);


ALTER TABLE public."user" OWNER TO postgres;

--
-- Name: logga_in_som_användare; Type: VIEW; Schema: public; Owner: postgres
--

CREATE VIEW public."logga_in_som_användare" AS
 SELECT b.id AS booking_id,
    h.hotel_name,
    h.city,
    t.start_date,
    t.end_date,
    p.payment_date,
    p.payment_type
   FROM (((public.booking b
     JOIN public.hotel h ON ((b.hotel_id = h.id)))
     JOIN public.travel t ON ((t.id = b.travel_id)))
     JOIN public.payment p ON ((p.id = b.payment_id)))
  WHERE (b.user_id = ( SELECT u.id
           FROM public."user" u
          WHERE (((u.email)::text = 'anna.berg@example.com'::text) AND ((u.password)::text = 'pass123'::text))));


ALTER VIEW public."logga_in_som_användare" OWNER TO postgres;

--
-- Name: payment_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.payment_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.payment_id_seq OWNER TO postgres;

--
-- Name: payment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.payment_id_seq OWNED BY public.payment.id;


--
-- Name: rating; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.rating (
    id integer NOT NULL,
    activites_id integer,
    name character varying(255),
    stars character varying(16),
    comment character varying(255)
);


ALTER TABLE public.rating OWNER TO postgres;

--
-- Name: rating_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.rating_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.rating_id_seq OWNER TO postgres;

--
-- Name: rating_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.rating_id_seq OWNED BY public.rating.id;


--
-- Name: room; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.room (
    id integer NOT NULL,
    room_type character varying(255),
    room_number integer,
    total_beds integer,
    max_adults integer,
    max_kids integer
);


ALTER TABLE public.room OWNER TO postgres;

--
-- Name: room_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.room_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.room_id_seq OWNER TO postgres;

--
-- Name: room_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.room_id_seq OWNED BY public.room.id;


--
-- Name: se_om_ett_boende_är_fullbokat; Type: VIEW; Schema: public; Owner: postgres
--

CREATE VIEW public."se_om_ett_boende_är_fullbokat" AS
 SELECT hotel_name,
    guest_limit,
    available
   FROM public.hotel
  ORDER BY available;


ALTER VIEW public."se_om_ett_boende_är_fullbokat" OWNER TO postgres;

--
-- Name: som_resenär_vill_jag_se_avgångs_och_ankomsttider; Type: VIEW; Schema: public; Owner: postgres
--

CREATE VIEW public."som_resenär_vill_jag_se_avgångs_och_ankomsttider" AS
 SELECT (((u.first_name)::text || ' '::text) || (u.last_name)::text) AS traveler_name,
    t.id AS travel_id,
    tr.departure_place,
    tr.arrival_place,
    tr.departure_time,
    tr.arrival_time,
    h.hotel_name,
    h.city AS hotel_city
   FROM ((((public.booking b
     JOIN public."user" u ON ((b.user_id = u.id)))
     JOIN public.travel t ON ((b.travel_id = t.id)))
     JOIN public.transport tr ON ((t.transport_id = tr.id)))
     JOIN public.hotel h ON ((b.hotel_id = h.id)))
  WHERE (((u.first_name)::text = 'Anna'::text) AND ((u.last_name)::text = 'Berg'::text))
  ORDER BY u.first_name, t.id;


ALTER VIEW public."som_resenär_vill_jag_se_avgångs_och_ankomsttider" OWNER TO postgres;

--
-- Name: sortera_sökresultat_efter_pris_betyg_eller_popularitet; Type: VIEW; Schema: public; Owner: postgres
--

CREATE VIEW public."sortera_sökresultat_efter_pris_betyg_eller_popularitet" AS
 SELECT h.hotel_name,
    h.city,
    h.reigon,
    r.stars,
    t.price
   FROM (((((public."user"
     JOIN public.booking b ON (("user".id = b.user_id)))
     JOIN public.travel t ON ((t.id = b.travel_id)))
     JOIN public.activites a ON ((t.id = a.travel_id)))
     JOIN public.rating r ON ((a.id = r.activites_id)))
     JOIN public.hotel h ON ((h.id = b.hotel_id)))
  ORDER BY r.stars DESC;


ALTER VIEW public."sortera_sökresultat_efter_pris_betyg_eller_popularitet" OWNER TO postgres;

--
-- Name: söka_efter_lediga_boenden_i_en_viss_region_och_tidsperiod; Type: VIEW; Schema: public; Owner: postgres
--

CREATE VIEW public."söka_efter_lediga_boenden_i_en_viss_region_och_tidsperiod" AS
 SELECT id AS hotel_id,
    hotel_name,
    city,
    country,
    guest_limit
   FROM public.hotel h
  WHERE ((((city)::text ~~* '%Paris%'::text) OR ((country)::text ~~* '%Frankrike%'::text)) AND (NOT (id IN ( SELECT DISTINCT b.hotel_id
           FROM (public.booking b
             JOIN public.travel t ON ((b.travel_id = t.id)))
          WHERE ((t.start_date <= '2025-07-15 00:00:00'::timestamp without time zone) AND ((t.end_date)::text >= '2025-07-10'::text))))))
  ORDER BY city, hotel_name;


ALTER VIEW public."söka_efter_lediga_boenden_i_en_viss_region_och_tidsperiod" OWNER TO postgres;

--
-- Name: transport_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.transport_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.transport_id_seq OWNER TO postgres;

--
-- Name: transport_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.transport_id_seq OWNED BY public.transport.id;


--
-- Name: travel_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.travel_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.travel_id_seq OWNER TO postgres;

--
-- Name: travel_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.travel_id_seq OWNED BY public.travel.id;


--
-- Name: user_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.user_id_seq OWNER TO postgres;

--
-- Name: user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_id_seq OWNED BY public."user".id;


--
-- Name: visar_hotell_där_man_kan_se_om_boendet_har_tillräcklig_kapaci; Type: VIEW; Schema: public; Owner: postgres
--

CREATE VIEW public."visar_hotell_där_man_kan_se_om_boendet_har_tillräcklig_kapaci" AS
 SELECT h.hotel_name,
    r.room_type,
    r.total_beds,
    booking.adults,
    booking.kids
   FROM (((public.booking
     JOIN public.hotel h ON ((h.id = booking.hotel_id)))
     JOIN public.booking_x_room bxr ON ((booking.id = bxr.booking_id)))
     JOIN public.room r ON ((r.id = bxr.room_id)));


ALTER VIEW public."visar_hotell_där_man_kan_se_om_boendet_har_tillräcklig_kapaci" OWNER TO postgres;

--
-- Name: activites id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.activites ALTER COLUMN id SET DEFAULT nextval('public.activites_id_seq'::regclass);


--
-- Name: booking id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.booking ALTER COLUMN id SET DEFAULT nextval('public.booking_id_seq'::regclass);


--
-- Name: hotel id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.hotel ALTER COLUMN id SET DEFAULT nextval('public.hotel_id_seq'::regclass);


--
-- Name: payment id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.payment ALTER COLUMN id SET DEFAULT nextval('public.payment_id_seq'::regclass);


--
-- Name: rating id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rating ALTER COLUMN id SET DEFAULT nextval('public.rating_id_seq'::regclass);


--
-- Name: room id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.room ALTER COLUMN id SET DEFAULT nextval('public.room_id_seq'::regclass);


--
-- Name: transport id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.transport ALTER COLUMN id SET DEFAULT nextval('public.transport_id_seq'::regclass);


--
-- Name: travel id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.travel ALTER COLUMN id SET DEFAULT nextval('public.travel_id_seq'::regclass);


--
-- Name: user id; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."user" ALTER COLUMN id SET DEFAULT nextval('public.user_id_seq'::regclass);


--
-- Data for Name: activites; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.activites (id, travel_id, resturant_name, activites_type, start_time, end_time) VALUES (1, 1, 'Le Gourmet', 'food', '2025-12-02 18:00:00', '2025-12-02 21:00:00');
INSERT INTO public.activites (id, travel_id, resturant_name, activites_type, start_time, end_time) VALUES (2, 2, 'Berlin Brewpub', 'beer', '2025-12-06 19:00:00', '2025-12-06 23:00:00');
INSERT INTO public.activites (id, travel_id, resturant_name, activites_type, start_time, end_time) VALUES (3, 3, 'London Tavern', 'beer', '2025-12-11 17:00:00', '2025-12-11 22:00:00');
INSERT INTO public.activites (id, travel_id, resturant_name, activites_type, start_time, end_time) VALUES (4, 4, 'Trattoria Roma', 'food', '2025-12-16 19:30:00', '2025-12-16 22:00:00');
INSERT INTO public.activites (id, travel_id, resturant_name, activites_type, start_time, end_time) VALUES (5, 5, 'Amsterdam Wine Bar', 'wine', '2025-12-21 18:00:00', '2025-12-21 21:00:00');
INSERT INTO public.activites (id, travel_id, resturant_name, activites_type, start_time, end_time) VALUES (6, 6, 'Madrid Tapas', 'food', '2025-12-26 19:00:00', '2025-12-26 22:00:00');
INSERT INTO public.activites (id, travel_id, resturant_name, activites_type, start_time, end_time) VALUES (7, 7, 'Copenhagen Bar', 'beer', '2025-12-31 18:00:00', '2025-12-31 23:00:00');
INSERT INTO public.activites (id, travel_id, resturant_name, activites_type, start_time, end_time) VALUES (8, 8, 'Oslo Kitchen', 'food', '2026-01-06 18:30:00', '2026-01-06 21:30:00');
INSERT INTO public.activites (id, travel_id, resturant_name, activites_type, start_time, end_time) VALUES (9, 9, 'Reykjavik Brewery', 'beer', '2026-01-11 18:00:00', '2026-01-11 22:00:00');
INSERT INTO public.activites (id, travel_id, resturant_name, activites_type, start_time, end_time) VALUES (10, 10, 'Vienna Wine House', 'wine', '2026-01-16 19:00:00', '2026-01-16 22:00:00');


--
-- Data for Name: booking; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.booking (id, user_id, travel_id, hotel_id, payment_id, adults, kids) VALUES (1, 1, 1, 1, 1, 2, 0);
INSERT INTO public.booking (id, user_id, travel_id, hotel_id, payment_id, adults, kids) VALUES (2, 2, 2, 2, 2, 1, 1);
INSERT INTO public.booking (id, user_id, travel_id, hotel_id, payment_id, adults, kids) VALUES (3, 3, 3, 3, 3, 2, 0);
INSERT INTO public.booking (id, user_id, travel_id, hotel_id, payment_id, adults, kids) VALUES (4, 4, 4, 4, 4, 1, 0);
INSERT INTO public.booking (id, user_id, travel_id, hotel_id, payment_id, adults, kids) VALUES (5, 5, 5, 5, 5, 2, 1);
INSERT INTO public.booking (id, user_id, travel_id, hotel_id, payment_id, adults, kids) VALUES (6, 6, 6, 6, 6, 2, 0);
INSERT INTO public.booking (id, user_id, travel_id, hotel_id, payment_id, adults, kids) VALUES (7, 7, 7, 7, 7, 1, 0);
INSERT INTO public.booking (id, user_id, travel_id, hotel_id, payment_id, adults, kids) VALUES (8, 8, 8, 8, 8, 2, 0);
INSERT INTO public.booking (id, user_id, travel_id, hotel_id, payment_id, adults, kids) VALUES (9, 9, 9, 9, 9, 2, 1);
INSERT INTO public.booking (id, user_id, travel_id, hotel_id, payment_id, adults, kids) VALUES (10, 10, 10, 10, 10, 1, 0);


--
-- Data for Name: booking_x_room; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.booking_x_room (booking_id, room_id) VALUES (1, 1);
INSERT INTO public.booking_x_room (booking_id, room_id) VALUES (2, 2);
INSERT INTO public.booking_x_room (booking_id, room_id) VALUES (3, 3);
INSERT INTO public.booking_x_room (booking_id, room_id) VALUES (4, 4);
INSERT INTO public.booking_x_room (booking_id, room_id) VALUES (5, 5);
INSERT INTO public.booking_x_room (booking_id, room_id) VALUES (6, 6);
INSERT INTO public.booking_x_room (booking_id, room_id) VALUES (7, 7);
INSERT INTO public.booking_x_room (booking_id, room_id) VALUES (8, 8);
INSERT INTO public.booking_x_room (booking_id, room_id) VALUES (9, 9);
INSERT INTO public.booking_x_room (booking_id, room_id) VALUES (10, 10);


--
-- Data for Name: hotel; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.hotel (id, reigon, city, country, hotel_name, guest_limit, available) VALUES (4, 'Lazio', 'Rome', 'Italy', 'Hotel Roma Bella', 120, 10);
INSERT INTO public.hotel (id, reigon, city, country, hotel_name, guest_limit, available) VALUES (5, 'North Holland', 'Amsterdam', 'Netherlands', 'Canal Stay', 140, 20);
INSERT INTO public.hotel (id, reigon, city, country, hotel_name, guest_limit, available) VALUES (8, 'Oslo', 'Oslo', 'Norway', 'Viking Hotel', 100, 40);
INSERT INTO public.hotel (id, reigon, city, country, hotel_name, guest_limit, available) VALUES (10, 'Vienna', 'Vienna', 'Austria', 'Kaiserhof', 110, 70);
INSERT INTO public.hotel (id, reigon, city, country, hotel_name, guest_limit, available) VALUES (3, 'Greater London', 'London', 'UK', 'The King’s Arms', 180, 120);
INSERT INTO public.hotel (id, reigon, city, country, hotel_name, guest_limit, available) VALUES (7, 'Hovedstaden', 'Copenhagen', 'Denmark', 'Nordic Light', 130, 100);
INSERT INTO public.hotel (id, reigon, city, country, hotel_name, guest_limit, available) VALUES (2, 'Berlin-Mitte', 'Berlin', 'Germany', 'Hotel Adler', 150, 0);
INSERT INTO public.hotel (id, reigon, city, country, hotel_name, guest_limit, available) VALUES (1, 'Île-de-France', 'Paris', 'France', 'Hotel Lumière', 200, 0);
INSERT INTO public.hotel (id, reigon, city, country, hotel_name, guest_limit, available) VALUES (6, 'Madrid', 'Madrid', 'Spain', 'Sol y Luna', 160, 40);
INSERT INTO public.hotel (id, reigon, city, country, hotel_name, guest_limit, available) VALUES (9, 'Reykjavik', 'Reykjavik', 'Iceland', 'Aurora Stay', 90, 20);


--
-- Data for Name: payment; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.payment (id, payment_type, payment_date) VALUES (10, 'paypal', '2025-11-30');
INSERT INTO public.payment (id, payment_type, payment_date) VALUES (9, 'credit_card', '2025-11-30');
INSERT INTO public.payment (id, payment_type, payment_date) VALUES (8, 'bank_transfer', '2025-11-30');
INSERT INTO public.payment (id, payment_type, payment_date) VALUES (5, 'bank_transfer', '2025-11-30');
INSERT INTO public.payment (id, payment_type, payment_date) VALUES (4, 'paypal', '2025-11-30');
INSERT INTO public.payment (id, payment_type, payment_date) VALUES (6, 'credit_card', '2025-11-30');
INSERT INTO public.payment (id, payment_type, payment_date) VALUES (7, 'paypal', '2025-11-30');
INSERT INTO public.payment (id, payment_type, payment_date) VALUES (2, 'bank_transfer', '2025-11-30');
INSERT INTO public.payment (id, payment_type, payment_date) VALUES (3, 'credit_card', '2025-11-30');
INSERT INTO public.payment (id, payment_type, payment_date) VALUES (1, 'paypal', '2025-11-30');


--
-- Data for Name: rating; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.rating (id, activites_id, name, stars, comment) VALUES (1, 1, 'Anna Berg', '5', 'Fantastisk mat och service!');
INSERT INTO public.rating (id, activites_id, name, stars, comment) VALUES (2, 2, 'Björn Nilsson', '4', 'Bra öl, men lite trångt.');
INSERT INTO public.rating (id, activites_id, name, stars, comment) VALUES (3, 3, 'Clara Svensson', '5', 'Underbar atmosfär!');
INSERT INTO public.rating (id, activites_id, name, stars, comment) VALUES (4, 4, 'David Lind', '3', 'Ganska bra, men lång väntetid.');
INSERT INTO public.rating (id, activites_id, name, stars, comment) VALUES (5, 5, 'Erik Johansson', '5', 'Bästa vinupplevelsen någonsin!');
INSERT INTO public.rating (id, activites_id, name, stars, comment) VALUES (6, 6, 'Frida Andersson', '4', 'God mat och trevlig personal.');
INSERT INTO public.rating (id, activites_id, name, stars, comment) VALUES (7, 7, 'Gustav Larsson', '5', 'Perfekt nyårsfirande!');
INSERT INTO public.rating (id, activites_id, name, stars, comment) VALUES (8, 8, 'Hanna Karlsson', '4', 'Bra service och mysig miljö.');
INSERT INTO public.rating (id, activites_id, name, stars, comment) VALUES (9, 9, 'Isak Olofsson', '3', 'Intressant lokal öl, men dyrt.');
INSERT INTO public.rating (id, activites_id, name, stars, comment) VALUES (10, 10, 'Johanna Pettersson', '5', 'Vin och musik i toppklass!');


--
-- Data for Name: room; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.room (id, room_type, room_number, total_beds, max_adults, max_kids) VALUES (1, 'single', 101, 1, 1, 0);
INSERT INTO public.room (id, room_type, room_number, total_beds, max_adults, max_kids) VALUES (2, 'double', 102, 2, 2, 1);
INSERT INTO public.room (id, room_type, room_number, total_beds, max_adults, max_kids) VALUES (3, 'double', 201, 2, 2, 1);
INSERT INTO public.room (id, room_type, room_number, total_beds, max_adults, max_kids) VALUES (4, 'single', 301, 1, 1, 0);
INSERT INTO public.room (id, room_type, room_number, total_beds, max_adults, max_kids) VALUES (5, 'double', 401, 2, 2, 1);
INSERT INTO public.room (id, room_type, room_number, total_beds, max_adults, max_kids) VALUES (6, 'single', 501, 1, 1, 0);
INSERT INTO public.room (id, room_type, room_number, total_beds, max_adults, max_kids) VALUES (7, 'double', 601, 2, 2, 1);
INSERT INTO public.room (id, room_type, room_number, total_beds, max_adults, max_kids) VALUES (8, 'single', 701, 1, 1, 0);
INSERT INTO public.room (id, room_type, room_number, total_beds, max_adults, max_kids) VALUES (9, 'double', 801, 2, 2, 1);
INSERT INTO public.room (id, room_type, room_number, total_beds, max_adults, max_kids) VALUES (10, 'single', 901, 1, 1, 0);


--
-- Data for Name: transport; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.transport (id, departure_time, departure_place, arrival_time, arrival_place, home_departure_time, home_departure_place, home_arrival_time, home_arrival_place, transport_during_travel) VALUES (1, '2025-12-01 08:00:00', 'Stockholm', '2025-12-01 12:00:00', 'Paris', '2025-11-30 18:00:00', 'Paris', '2025-12-10 22:00:00', 'Stockholm', 'Metro, taxi, bus in Paris');
INSERT INTO public.transport (id, departure_time, departure_place, arrival_time, arrival_place, home_departure_time, home_departure_place, home_arrival_time, home_arrival_place, transport_during_travel) VALUES (2, '2025-12-05 09:00:00', 'Gothenburg', '2025-12-05 11:00:00', 'Berlin', '2025-12-04 17:00:00', 'Berlin', '2025-12-14 21:00:00', 'Gothenburg', 'Tram and bus within Berlin');
INSERT INTO public.transport (id, departure_time, departure_place, arrival_time, arrival_place, home_departure_time, home_departure_place, home_arrival_time, home_arrival_place, transport_during_travel) VALUES (3, '2025-12-10 07:30:00', 'Malmö', '2025-12-10 10:30:00', 'London', '2025-12-09 18:00:00', 'London', '2025-12-17 20:00:00', 'Malmö', 'Underground, bus, and train in London');
INSERT INTO public.transport (id, departure_time, departure_place, arrival_time, arrival_place, home_departure_time, home_departure_place, home_arrival_time, home_arrival_place, transport_during_travel) VALUES (4, '2025-12-15 10:00:00', 'Stockholm', '2025-12-15 14:00:00', 'Rome', '2025-12-14 19:00:00', 'Rome', '2025-12-23 23:00:00', 'Stockholm', 'Metro and taxi in Rome');
INSERT INTO public.transport (id, departure_time, departure_place, arrival_time, arrival_place, home_departure_time, home_departure_place, home_arrival_time, home_arrival_place, transport_during_travel) VALUES (5, '2025-12-20 09:00:00', 'Uppsala', '2025-12-20 13:00:00', 'Amsterdam', '2025-12-19 18:00:00', 'Amsterdam', '2025-12-28 22:00:00', 'Uppsala', 'Bike and tram in Amsterdam');
INSERT INTO public.transport (id, departure_time, departure_place, arrival_time, arrival_place, home_departure_time, home_departure_place, home_arrival_time, home_arrival_place, transport_during_travel) VALUES (6, '2025-12-25 08:00:00', 'Stockholm', '2025-12-25 16:00:00', 'Madrid', '2025-12-24 19:00:00', 'Madrid', '2026-01-02 22:00:00', 'Stockholm', 'Metro, taxi, and train in Madrid');
INSERT INTO public.transport (id, departure_time, departure_place, arrival_time, arrival_place, home_departure_time, home_departure_place, home_arrival_time, home_arrival_place, transport_during_travel) VALUES (7, '2025-12-30 11:00:00', 'Lund', '2025-12-30 15:00:00', 'Copenhagen', '2025-12-29 18:00:00', 'Copenhagen', '2026-01-05 20:00:00', 'Lund', 'Metro and bicycle in Copenhagen');
INSERT INTO public.transport (id, departure_time, departure_place, arrival_time, arrival_place, home_departure_time, home_departure_place, home_arrival_time, home_arrival_place, transport_during_travel) VALUES (8, '2026-01-05 07:00:00', 'Stockholm', '2026-01-05 13:00:00', 'Oslo', '2026-01-04 19:00:00', 'Oslo', '2026-01-12 22:00:00', 'Stockholm', 'Bus and metro in Oslo');
INSERT INTO public.transport (id, departure_time, departure_place, arrival_time, arrival_place, home_departure_time, home_departure_place, home_arrival_time, home_arrival_place, transport_during_travel) VALUES (9, '2026-01-10 09:00:00', 'Stockholm', '2026-01-10 12:00:00', 'Reykjavik', '2026-01-09 18:00:00', 'Reykjavik', '2026-01-18 21:00:00', 'Stockholm', 'Bus and taxi in Reykjavik');
INSERT INTO public.transport (id, departure_time, departure_place, arrival_time, arrival_place, home_departure_time, home_departure_place, home_arrival_time, home_arrival_place, transport_during_travel) VALUES (10, '2026-01-15 10:00:00', 'Malmö', '2026-01-15 14:00:00', 'Vienna', '2026-01-14 19:00:00', 'Vienna', '2026-01-23 22:00:00', 'Malmö', 'Metro and tram in Vienna');


--
-- Data for Name: travel; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.travel (id, transport_id, start_date, end_date, price) VALUES (1, 1, '2025-12-01 00:00:00', '2025-12-10', '1200 EUR');
INSERT INTO public.travel (id, transport_id, start_date, end_date, price) VALUES (2, 2, '2025-12-05 00:00:00', '2025-12-14', '1000 EUR');
INSERT INTO public.travel (id, transport_id, start_date, end_date, price) VALUES (3, 3, '2025-12-10 00:00:00', '2025-12-17', '1500 EUR');
INSERT INTO public.travel (id, transport_id, start_date, end_date, price) VALUES (4, 4, '2025-12-15 00:00:00', '2025-12-23', '1100 EUR');
INSERT INTO public.travel (id, transport_id, start_date, end_date, price) VALUES (5, 5, '2025-12-20 00:00:00', '2025-12-28', '1300 EUR');
INSERT INTO public.travel (id, transport_id, start_date, end_date, price) VALUES (6, 6, '2025-12-25 00:00:00', '2026-01-02', '1600 EUR');
INSERT INTO public.travel (id, transport_id, start_date, end_date, price) VALUES (7, 7, '2025-12-30 00:00:00', '2026-01-05', '900 EUR');
INSERT INTO public.travel (id, transport_id, start_date, end_date, price) VALUES (8, 8, '2026-01-05 00:00:00', '2026-01-12', '1400 EUR');
INSERT INTO public.travel (id, transport_id, start_date, end_date, price) VALUES (9, 9, '2026-01-10 00:00:00', '2026-01-18', '1250 EUR');
INSERT INTO public.travel (id, transport_id, start_date, end_date, price) VALUES (10, 10, '2026-01-15 00:00:00', '2026-01-23', '1550 EUR');


--
-- Data for Name: user; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public."user" (id, first_name, last_name, email, password) VALUES (1, 'Anna', 'Berg', 'anna.berg@example.com', 'pass123');
INSERT INTO public."user" (id, first_name, last_name, email, password) VALUES (2, 'Björn', 'Nilsson', 'bjorn.nilsson@example.com', 'pass123');
INSERT INTO public."user" (id, first_name, last_name, email, password) VALUES (3, 'Clara', 'Svensson', 'clara.s@example.com', 'pass123');
INSERT INTO public."user" (id, first_name, last_name, email, password) VALUES (4, 'David', 'Lind', 'david.l@example.com', 'pass123');
INSERT INTO public."user" (id, first_name, last_name, email, password) VALUES (5, 'Erik', 'Johansson', 'erik.j@example.com', 'pass123');
INSERT INTO public."user" (id, first_name, last_name, email, password) VALUES (6, 'Frida', 'Andersson', 'frida.a@example.com', 'pass123');
INSERT INTO public."user" (id, first_name, last_name, email, password) VALUES (7, 'Gustav', 'Larsson', 'gustav.l@example.com', 'pass123');
INSERT INTO public."user" (id, first_name, last_name, email, password) VALUES (8, 'Hanna', 'Karlsson', 'hanna.k@example.com', 'pass123');
INSERT INTO public."user" (id, first_name, last_name, email, password) VALUES (9, 'Isak', 'Olofsson', 'isak.o@example.com', 'pass123');
INSERT INTO public."user" (id, first_name, last_name, email, password) VALUES (10, 'Johanna', 'Pettersson', 'johanna.p@example.com', 'pass123');
INSERT INTO public."user" (id, first_name, last_name, email, password) VALUES (11, 'Karin', 'Bengtsson', 'karin.b@example.com', 'pass123');
INSERT INTO public."user" (id, first_name, last_name, email, password) VALUES (12, 'Leo', 'Lund', 'leo.l@example.com', 'pass123');
INSERT INTO public."user" (id, first_name, last_name, email, password) VALUES (13, 'Maria', 'Holm', 'maria.h@example.com', 'pass123');
INSERT INTO public."user" (id, first_name, last_name, email, password) VALUES (14, 'Niklas', 'Persson', 'niklas.p@example.com', 'pass123');
INSERT INTO public."user" (id, first_name, last_name, email, password) VALUES (15, 'Olivia', 'Sundberg', 'olivia.s@example.com', 'pass123');
INSERT INTO public."user" (id, first_name, last_name, email, password) VALUES (16, 'Patrik', 'Ek', 'patrik.e@example.com', 'pass123');
INSERT INTO public."user" (id, first_name, last_name, email, password) VALUES (17, 'Quinn', 'Wiklund', 'quinn.w@example.com', 'pass123');
INSERT INTO public."user" (id, first_name, last_name, email, password) VALUES (18, 'Rasmus', 'Blom', 'rasmus.b@example.com', 'pass123');
INSERT INTO public."user" (id, first_name, last_name, email, password) VALUES (19, 'Sara', 'Norén', 'sara.n@example.com', 'pass123');
INSERT INTO public."user" (id, first_name, last_name, email, password) VALUES (20, 'Tobias', 'Åkesson', 'tobias.a@example.com', 'pass123');


--
-- Name: activites_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.activites_id_seq', 10, true);


--
-- Name: booking_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.booking_id_seq', 10, true);


--
-- Name: hotel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.hotel_id_seq', 10, true);


--
-- Name: payment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.payment_id_seq', 10, true);


--
-- Name: rating_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.rating_id_seq', 10, true);


--
-- Name: room_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.room_id_seq', 10, true);


--
-- Name: transport_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.transport_id_seq', 10, true);


--
-- Name: travel_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.travel_id_seq', 10, true);


--
-- Name: user_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_id_seq', 20, true);


--
-- Name: activites activites_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.activites
    ADD CONSTRAINT activites_pk PRIMARY KEY (id);


--
-- Name: booking booking_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.booking
    ADD CONSTRAINT booking_pk PRIMARY KEY (id);


--
-- Name: hotel hotel_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.hotel
    ADD CONSTRAINT hotel_pk PRIMARY KEY (id);


--
-- Name: payment payment_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.payment
    ADD CONSTRAINT payment_pk PRIMARY KEY (id);


--
-- Name: rating rating_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rating
    ADD CONSTRAINT rating_pk PRIMARY KEY (id);


--
-- Name: room room_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.room
    ADD CONSTRAINT room_pk PRIMARY KEY (id);


--
-- Name: transport transport_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.transport
    ADD CONSTRAINT transport_pk PRIMARY KEY (id);


--
-- Name: travel travel_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.travel
    ADD CONSTRAINT travel_pk PRIMARY KEY (id);


--
-- Name: user user_pk; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pk PRIMARY KEY (id);


--
-- Name: activites activites_travel_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.activites
    ADD CONSTRAINT activites_travel_id_fk FOREIGN KEY (travel_id) REFERENCES public.travel(id);


--
-- Name: booking booking_hotel_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.booking
    ADD CONSTRAINT booking_hotel_id_fk FOREIGN KEY (hotel_id) REFERENCES public.hotel(id);


--
-- Name: booking booking_payment_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.booking
    ADD CONSTRAINT booking_payment_id_fk FOREIGN KEY (payment_id) REFERENCES public.payment(id);


--
-- Name: booking booking_travel_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.booking
    ADD CONSTRAINT booking_travel_id_fk FOREIGN KEY (travel_id) REFERENCES public.travel(id);


--
-- Name: booking booking_user_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.booking
    ADD CONSTRAINT booking_user_id_fk FOREIGN KEY (user_id) REFERENCES public."user"(id);


--
-- Name: booking_x_room booking_x_room_booking_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.booking_x_room
    ADD CONSTRAINT booking_x_room_booking_id_fk FOREIGN KEY (booking_id) REFERENCES public.booking(id);


--
-- Name: booking_x_room booking_x_room_room_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.booking_x_room
    ADD CONSTRAINT booking_x_room_room_id_fk FOREIGN KEY (room_id) REFERENCES public.room(id);


--
-- Name: rating rating_activites_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.rating
    ADD CONSTRAINT rating_activites_id_fk FOREIGN KEY (activites_id) REFERENCES public.activites(id);


--
-- Name: travel travel_transport_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.travel
    ADD CONSTRAINT travel_transport_id_fk FOREIGN KEY (transport_id) REFERENCES public.transport(id);


--
-- PostgreSQL database dump complete
--

\unrestrict TsVMCkeb8lNUpjBWkCpmQc4yyUILnd2pggsE1P6dF1apXZhY1rNlnQXHzidlUiD

