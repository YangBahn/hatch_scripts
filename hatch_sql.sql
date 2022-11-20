UPDATE user_debug
SET debug_level = 'NONE'
WHERE updatedAt > DATEADD(Day,-10,GETDATE());