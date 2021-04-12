use std::net::UdpSocket;

fn main() -> std::io::Result<()> {
    {
        let mut socket = UdpSocket::bind("127.0.0.1:34254")?;

        // Recibe un datagrama. Si el mensaje es muy grande, lo corta.
        let mut buf = [0; 10];
        let (amt, src) = socket.recv_from(&mut buf)?;
    }
    Ok(())
}
