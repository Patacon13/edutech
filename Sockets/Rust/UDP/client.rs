use std::net::UdpSocket;

fn main() -> std::io::Result<()> {
    {
        let mut socket = UdpSocket::bind("127.0.0.1:34255")?;

        let buf = u8::MAX >> 2;
        socket.send_to(&[buf], "127.0.0.1:34254")?; //se envia el mensaje al server
    }
    Ok(())
}
