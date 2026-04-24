ORIENTATION_QUERY = """
SELECT
    g.tilt,
    g.roll,
    g.azimuth
FROM geometry g

-- join camera associated with this geometry
JOIN camera c ON g.cameraID = c.id

-- join station associated with the camera
JOIN station st ON c.stationID = st.id


WHERE

-- filter by station identifier
    st.shortName = %s

-- filter by camera number
    AND c.cameraNumber = %s

-- ensure station is valid at given timestamp
    AND st.timeIN <= %s
    AND (st.timeOUT = 0 OR st.timeOUT >= %s)

-- ensure camera is valid at given timestamp
    AND c.timeIN <= %s
    AND (c.timeOUT = 0 OR c.timeOUT >= %s)

-- geometry must also be valid
    AND g.whenValid <= %s

-- get most recent valid geometry
ORDER BY g.whenValid DESC
LIMIT 1
"""