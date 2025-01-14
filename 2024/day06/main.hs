import Data.List (sortBy)
import Data.List (find)
import Data.Maybe (listToMaybe)

myElem :: Int -> [Int] -> Bool
myElem _ [] = False
myElem k (x:xs)
    | k == x    = True
    | otherwise = myElem k xs

mySort :: [Int] -> Bool
mySort [] = True
mySort [x] = True
mySort (x:y:xs)
    | x > y     = False
    | otherwise = mySort (y:xs)

sumEven :: [Int] -> Int
sumEven xs = sum (filter (\x -> x `mod` 2 == 0) xs)

sqList :: [Int] -> [Int]
sqList xs = map (\x -> x * x) xs

findMax :: [Int] -> Int
findMax xs = foldl (\acc x -> if x > acc then x else acc) (head xs) xs

doubleOdd :: [Int] -> [Int]
doubleOdd xs = map (\x ->  x * 2 ) $ filter (\x -> x `mod` 2 /= 0) xs

sortByLength :: [String] -> [String]
sortByLength xs = sortBy (\a b -> compare (length a) (length b)) xs

sumPairs :: [(Int, Int)] -> [Int]
sumPairs xs = map (\(x, y) -> x + y) xs

findCoordinates :: Eq a => a -> [[a]] -> Maybe (Int, Int)
findCoordinates num matrix = listToMaybe 
        [(r, c) | (r, row) <- zip [0..] matrix,(c, val) <- zip [0..] row, val == num]




main :: IO()
main = do
    print (myElem 2 [1,2,3])
    print (myElem 2 [1,4,3])

    print (mySort [1,2,3])
    print (mySort [1,4,3])

    print (sumEven [1,4,2])

    print (sqList [1,2,3])

    print (findMax [1,27,3])

    print (doubleOdd [1,2,3])

    print (sortByLength ["a","abc","ab"])

    print (sumPairs [(1,2),(2,3),(3,4)])


    contents <- readFile "in/in.test"
    let grid = lines contents
    print (findCoordinates '^' grid)