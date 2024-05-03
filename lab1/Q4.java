import java.util.*;


class Node {
    int[] state;
    Node parent;
    String action;
    int cost;


    public Node(int[] state, Node parent, String action, int cost) {
        this.state = state;
        this.parent = parent;
        this.action = action;
        this.cost = cost;
    }
}


public class Q4 {


    public static List<String> uniformCostSearch(int[] initialState, int[] goalState,
            Map<String, List<int[]>> getNeighbors) {
        PriorityQueue<Node> frontier = new PriorityQueue<>(Comparator.comparingInt(node -> node.cost));
        Set<String> explored = new HashSet<>();


        Node initialNode = new Node(initialState, null, null, 0);
        frontier.add(initialNode);


        while (!frontier.isEmpty()) {
            Node currentNode = frontier.poll();


            if (Arrays.equals(currentNode.state, goalState)) {
                return reconstructPath(currentNode);
            }


            explored.add(Arrays.toString(currentNode.state));


            List<int[]> neighbors = getNeighbors.getOrDefault(Arrays.toString(currentNode.state), new ArrayList<>());
            for (int[] neighbor : neighbors) {
                String neighborString = Arrays.toString(neighbor);
                if (!explored.contains(neighborString)) {
                    int newCost = currentNode.cost + 1;
                    Node newNode = new Node(neighbor, currentNode, neighborString, newCost);
                    frontier.add(newNode);
                }
            }
        }


        return null;
    }


    public static List<String> reconstructPath(Node node) {
        List<String> path = new ArrayList<>();
        while (node != null) {
            path.add(node.action);
            node = node.parent;
        }
        Collections.reverse(path);
        return path;
    }


    public static void main(String[] args) {
        Map<String, List<int[]>> getNeighbors = new HashMap<>();
        getNeighbors.put(Arrays.toString(new int[] { 0, 0 }), Arrays.asList(new int[] { 1, 0 }, new int[] { 0, 1 }));
        getNeighbors.put(Arrays.toString(new int[] { 1, 0 }), Arrays.asList(new int[] { 2, 0 }, new int[] { 1, 1 }));
        getNeighbors.put(Arrays.toString(new int[] { 0, 1 }), Arrays.asList(new int[] { 1, 1 }, new int[] { 0, 2 }));
        getNeighbors.put(Arrays.toString(new int[] { 1, 1 }),
                Arrays.asList(new int[] { 1, 0 }, new int[] { 1, 2 }, new int[] { 0, 1 }));
        getNeighbors.put(Arrays.toString(new int[] { 2, 0 }), Arrays.asList(new int[] { 3, 0 }, new int[] { 2, 1 }));


        int[] initialState = { 0, 0 };
        int[] goalState = { 2, 1 };
        List<String> path = uniformCostSearch(initialState, goalState, getNeighbors);


        if (path != null) {
            System.out.println("Path found: " + path);
        } else {
            System.out.println("No path found.");
        }
    }
}
