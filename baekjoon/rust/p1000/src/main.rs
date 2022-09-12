use std::io;
fn main() {
    let mut line = String::new();

    io::stdin().read_line(&mut line).unwrap();

    let values: Vec<&str> = line.split_whitespace().collect();

    println!("{line}");
    println!("{values:?}");

    let ints: Vec<i32> = values.map(|s| s.parse().unwrap()).collect();
}
