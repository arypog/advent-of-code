import Data.Maybe (listToMaybe)

type Position = (Int, Int)
type Antena = (Char, Position)
 
parse :: [String] -> Maybe [Antena]
parse grid = map fst (filter (\pos -> getPos pos grid) grid)

getPos :: 

main :: IO ()
main = do
    contents <- readFile "in/in.test"

    -- contents <- readFile "in/in.pub"
    print $ parse (lines contents)