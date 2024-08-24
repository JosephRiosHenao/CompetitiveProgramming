package Algorithms.Sorts.Java;

import java.util.ArrayList;
import java.util.Random;

/**
 * main
 */
public class Sorts {
    public static final int MAX = 20;
    public static final int MIN = 1;
    public static final int NUM = 10; 

    public static void main(String[] args) {
        Sorts sorter = new Sorts();
        ArrayList<Integer> seed = GenerateNumbers.getNumbers(MAX,MIN,NUM);
        System.out.println("Bubble Sort is: "+sorter.BubbleSort(seed));
        System.out.println("\n");
        seed = GenerateNumbers.getNumbers(MAX,MIN,NUM);
        System.out.println("Selection Sort is: "+sorter.SelectionSort(seed));
        System.out.println("\n");
        seed = GenerateNumbers.getNumbers(MAX,MIN,NUM);
        System.out.println("Insertion Sort is: "+sorter.InsertionSort(seed));
        System.out.println("\n");
        seed = GenerateNumbers.getNumbers(MAX,MIN,NUM);
        System.out.println("Merge Sort is: "+sorter.MergeSort(seed));
        System.out.println("\n");
        seed = GenerateNumbers.getNumbers(MAX,MIN,NUM);
        System.out.println("Counting Sort is: "+sorter.CountingSort(seed, MAX));
        System.out.println("\n");
        seed = GenerateNumbers.getNumbers(MAX,MIN,NUM);
        System.out.println("Quick Sort is: "+sorter.QuickSort(seed, 0, seed.size()-1));
    }

    public ArrayList<Integer> BubbleSort(ArrayList<Integer> seed){
        for (int idx = 0; idx < seed.size(); idx++) {
            for (int idj = 0; idj < seed.size()-1; idj++) {
                int actualNumber = seed.get(idj);
                int proxNumber = seed.get(idj+1);
                if (actualNumber > proxNumber){
                    seed.set(idj, proxNumber);
                    seed.set(idj+1, actualNumber);
                }
            }
        }
        return seed;
    }

    public ArrayList<Integer> SelectionSort(ArrayList<Integer> seed){
        for (int idx = 0; idx < seed.size(); idx++) {
            int minimumPosition = idx;
            for (int idj = idx+1; idj < seed.size(); idj++) {
                if (seed.get(minimumPosition) > seed.get(idj)){
                    minimumPosition = idj;
                }
            }
            if (minimumPosition != idx){
                int actualNumber = seed.get(idx);
                int changeNumber = seed.get(minimumPosition);
                seed.set(idx, changeNumber);
                seed.set(minimumPosition, actualNumber);
            }
        }
        return seed;
    }

    public ArrayList<Integer> InsertionSort(ArrayList<Integer> seed) {
        for (int idx = 1; idx < seed.size(); idx++) {
            int actualNumber = seed.get(idx);
            int i = idx - 1;
            while (i >= 0 && seed.get(i) > actualNumber) {
                seed.set(i + 1, seed.get(i));
                i--;
            }
            seed.set(i + 1, actualNumber);
        }
        return seed;
    }
    
    public ArrayList<Integer> MergeSort(ArrayList<Integer> seed) {
        if (seed.size() <= 1) {
            return seed;
        }

        int mid = seed.size() / 2;
        ArrayList<Integer> left = new ArrayList<>(seed.subList(0, mid));
        ArrayList<Integer> right = new ArrayList<>(seed.subList(mid, seed.size()));

        left = MergeSort(left);
        right = MergeSort(right);

        return merge(left, right);
    }


    private ArrayList<Integer> merge(ArrayList<Integer> left, ArrayList<Integer> right) {
        ArrayList<Integer> merged = new ArrayList<>();
        int i = 0, j = 0;

        while (i < left.size() && j < right.size()) {
            if (left.get(i) <= right.get(j)) {
                merged.add(left.get(i));
                i++;
            } else {
                merged.add(right.get(j));
                j++;
            }
        }

        while (i < left.size()) {
            merged.add(left.get(i));
            i++;
        }

        while (j < right.size()) {
            merged.add(right.get(j));
            j++;
        }

        return merged;
    }


    public class GenerateNumbers {
        public static ArrayList<Integer> getNumbers(int max, int min, int num){
            ArrayList<Integer> numbers = new ArrayList<>();
            Random generator = new Random();
            int randomNumber;
            for (int i = 0; i < num; i++) {
                randomNumber = generator.nextInt(min, max+1);
                numbers.add(randomNumber);
            }
            return numbers;
        }
    }
    

    public ArrayList<Integer> QuickSort(ArrayList<Integer> seed, int low, int high) {
        if (low < high) {
            int pivotIndex = partition(seed, low, high);
            QuickSort(seed, low, pivotIndex - 1);
            QuickSort(seed, pivotIndex + 1, high);
        }
        return seed;
    }

    private int partition(ArrayList<Integer> seed, int low, int high) {
        int pivot = seed.get(high); 
        int i = low - 1; 
        for (int j = low; j < high; j++) {
            if (seed.get(j) <= pivot) {
                i++;
                int temp = seed.get(i);
                seed.set(i, seed.get(j));
                seed.set(j, temp);
            }
        }
        int temp = seed.get(i + 1);
        seed.set(i + 1, seed.get(high));
        seed.set(high, temp);
        return i + 1; 
    }

    public ArrayList<Integer> CountingSort(ArrayList<Integer> seed, int max){
        int[] freq = new int[max+1];
        for (int idx = 0; idx < seed.size(); idx++) {
            freq[seed.get(idx)]= freq[idx]+1;
        }
        seed.clear();
        for (int idx = 0; idx < freq.length; idx++) {
            int actualNumber = freq[idx];
            if (actualNumber == 0) continue;
            for (int i = 0; i < freq[idx]; i++) {
                seed.add(idx);
            }
        }
        return seed;
    }
}
