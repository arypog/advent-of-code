import Data.List (elemIndex)
import qualified Data.Set as Set

type Direction = (Int, Int)

directions :: [Direction]
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  -- top, right, bottom, left

findGuardStartPos :: Char -> [[Char]] -> Maybe (Int, Int)
findGuardStartPos x matrix =
    let rowWithIndex = zip [0..] matrix
    in foldr (\(rowIdx, row) acc ->
                case elemIndex x row of
                    Just colIdx -> Just (rowIdx, colIdx)
                    Nothing -> acc
            ) Nothing rowWithIndex

startPatrol :: (Int, Int) -> [[Char]] -> Set.Set (Int, Int, Int)
startPatrol guardPos matrix = findPatrolPath (fst guardPos) (snd guardPos) 0 matrix Set.empty

isInBound :: Int -> Int -> [[Char]] -> Bool
isInBound x y matrix = x >= 0 && x < length matrix && y >= 0 && y < length (head matrix)

isObstruction :: Int -> Int -> [[Char]] -> Bool
isObstruction x y matrix = (matrix !! x) !! y == '#'

findPatrolPath :: Int -> Int -> Int -> [[Char]] -> Set.Set (Int, Int, Int) -> Set.Set (Int, Int, Int) 
findPatrolPath guardX guardY directionIndex matrix visited
    | not (isInBound nextX nextY matrix) = visited
    | isObstruction nextX nextY matrix = findPatrolPath guardX guardY newDirectionIndex matrix newVisited
    | Set.member (nextX, nextY, directionIndex) visited = visited
    | otherwise = findPatrolPath nextX nextY directionIndex matrix newVisited
  where
    (dx, dy) = directions !! directionIndex

    nextX = guardX + dx
    nextY = guardY + dy

    newDirectionIndex = (directionIndex + 1) `mod` 4

    newVisited = Set.insert (guardX, guardY, directionIndex) visited

findLoopingObstructions :: (Int, Int) -> [[Char]] -> Int -> Int
findLoopingObstructions matrix guardStartPos counter = 
    let patrolPath = startPatrol guardStartPos matrix


main :: IO ()
main = do
    -- contents <- readFile "in/in.pub"
    contents <- readFile "in/in.test"
    let matrix = lines contents

    case findGuardStartPos '^' matrix of
        Just guardPos -> do 
            --let patrolPath = startPatrol guardPos matrix
            let result = findLoopingObstructions matrix guardPos
            print result
            --print ((Set.size patrolPath) + 1)
        Nothing -> putStrLn "Guard not found"
