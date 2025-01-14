import Control.Monad (sequence)

parse :: [String] -> [(Int, [Int])]
parse = map parseLine . filter (not . null)

parseLine :: String -> (Int, [Int])
parseLine line =
    let parts = words (filter (/= ':') line)
        target = read (head parts) :: Int
        numbers = map read (tail parts)
    in (target, numbers)

concatOp :: Int -> Int -> Int
concatOp a b = read (show a ++ show b)

operatorCombinations :: Int -> [Int -> Int -> Int] -> [[(Int -> Int -> Int)]]
operatorCombinations n ops = sequence (replicate (n - 1) ops)

applyOperators :: [Int] -> [(Int -> Int -> Int)] -> Int
applyOperators (x:y:xs) (op:ops) = applyOperators (op x y : xs) ops
applyOperators [x] [] = x

evaluate :: (Int, [Int]) -> [Int -> Int -> Int] -> Bool
evaluate (target, nums) ops =
    target `elem` allEvaluations nums ops

allEvaluations :: [Int] -> [Int -> Int -> Int] -> [Int]
allEvaluations [] _ = []
allEvaluations [x] _ = [x]
allEvaluations xs ops = 
    [ result | opsCombo <- operatorCombinations (length xs) ops,
               let result = applyOperators xs opsCombo ]

part1 :: [(Int, [Int])] -> Int
part1 equations = 
    sum (map fst (filter (\eq -> evaluate eq [ (+), (*) ]) equations))

part2 :: [(Int, [Int])] -> Int
part2 equations = 
    sum (map fst (filter (\eq -> evaluate eq [ (+), (*), concatOp ]) equations))

main :: IO ()
main = do
    -- contents <- readFile "in/in.test"
    contents <- readFile "in/in.pub"
    let equations = parse (lines contents)

    print part1 equations
    
    print part2 equations



