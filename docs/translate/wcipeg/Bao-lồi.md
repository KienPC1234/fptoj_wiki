Trong hình học tính toán, bao lồi của một tập điểm là tập lồi nhỏ nhất (theo diện tích, thể tích, ...) mà tất cả các điểm đều nằm trong tập đó.


- Nếu ta coi các điểm trong một tập hợp là các cái đinh đóng trên một tấm gỗ, bao lồi của tập điểm đó có viền ngoài tạo bởi sợi dây chun mắc vào các cái đinh sau khi bị kéo căng về các phía.

- Nếu ta coi các điểm trong một tập hợp là các con cừu trên đồng cỏ, bao lồi của tập điểm đó có viền ngoài là hàng rào có độ dài nhỏ nhất bao quanh tất cả các con cừu

- Nếu ta coi các điểm trong một tập hợp là các đầu mút có thể của các hàng rào, bao lồi của tập điểm đó có viền ngoài là các hàng rào thẳng có điểm đầu và điểm cuối thuộc tập điểm đó và bao quanh diện tích lớn nhất.

- Nếu ta coi các điểm trong một tập hợp là các cái cây, chu vi của bao lồi là độ dài tối thiểu của dải ruy băng bao quanh tất cả các cây đó.

## Thuật toán tìm bao lồi trên mặt phẳng

Bài toán tìm bao lồi của một tập điểm trên mặt phẳng là một trong những bài toán được nghiên cứu nhiều nhất trong hình học tính toán và có rất nhiều thuật toán để giải bài toán này. Sau đây là ba thuật toán phổ biến nhất, được giới thiệu theo thứ tự tăng dần về độ khó.

## Thuật toán bọc gói

Thuật toán bọc gói hay còn gọi là thuật toán Jarvis march là một trong những thuật toán tìm bao lồi đơn giản và dễ hiểu nhất. Tên thuật toán xuất phát từ sự tương tự của thuật toán với việc đi bộ xung quanh các điểm và cầm theo một dải băng gói quà.

Bước đầu tiên của thuật toán là chọn một điểm chắc chắn nằm trong bao lồi, ví dụ, điểm có tung độ lớn nhất. Bắt đầu từ điểm này, ta sẽ lần lượt đi đến các điểm khác cho đến khi quay trở lại điểm ta chọn lúc đầu. Sau đó, ta nhìn về phía bên phải điểm ta vừa chọn. Tại mỗi thời điểm ta sẽ lưu lại vi trí điểm $P$ mà ta đang chọn và vector $\vec{v}$ chỉ hướng ta đang nhìn. Tiếp theo, thuật toán sẽ lặp lại liên tục các bước sau cho đến khi tìm được bao lồi. Ta quay mặt theo chiều kim đồng hồ cho đến khi ta nhìn thấy một điểm, gọi điểm đó là $Q$. Rồi ta cầm theo dải băng và đi đến điểm $Q$. Khi ta đến điểm đấy, $\vec{v}$ trở thành $\vec{PQ}$ và $P$ trở thành $Q$. Khi thuật toán kết thúc, ta đã đi đến tất cả các đỉnh của bao lồi theo chiều kim đồng hồ.

Để xác định điểm ta nhìn thấy đầu tiên khi ta quay mặt theo chiều kim đồng hồ, ta duyệt tất cả các điểm $R$ trong tập, ngoại trừ điểm $P$, với mỗi điểm, ta xét vector $\vec{u}=\vec{PR}$. $\vec{u}$ tạo với $\vec{v}$ một góc $\theta$ nhỏ nhất sẽ tương ứng với điểm $Q$ (dễ dàng chứng minh được điều này). Để tìm $\theta$ nhỏ nhất, ta tìm $\cos{ \theta }$ lớn nhất, mà ta lại dễ dàng tính được $\cos{ \theta }$ bằng công thức $\frac{\vec{u}.\vec{v}}{\|\vec{u}\|\|\vec{v}\|}$

Với mỗi lần tìm điểm tiếp theo, ta cần duyệt qua tất cả các điểm trong tập, vì vậy độ phức tạp của mỗi lần tìm điểm là $O(n)$ với $n$ là số lượng điểm trong tập. Số lần tìm điểm tiếp theo phụ thuộc vào số lượng điểm là đỉnh của bao lồi, gọi số lượng điểm đó là $h$, vì vậy độ phức tạp của cả thuật toán là $O(nh)$. Trong trường hợp xấu nhất, $h=n$ hay tất cả các điểm trong dữ liệu vào tạo thành một đa giác lồi, độ phức tạp của thuật toán là $O(n^2)$, không đủ nhanh khi $n > 5000$.

## Thuật toán Graham
Thuật toán Graham có độ phức tạp trong trường hợp xấu nhất nhỏ hơn thuật toán bọc gói, song thuật toán Graham lại phức tạp hơn. Đầu tiên, một điểm (không nhất thiết phải có trong dữ liệu vào) mà chắc chắn thuộc vào bao được xác định. Tìm giá trị trung bình của hoành độ và tung độ các điểm trong dữ liệu là một cách để tìm tọa độ của một điểm như vậy. Sau đó ta chọn hệ trục tọa độ có gốc là điểm vừa chọn, sau đó đổi tọa độ các điểm còn lại theo hệ trục tọa độ mới (trong thực tế ta sẽ không làm như vậy). Tiếp theo, ta sắp xếp các điểm $P$ còn lại theo thứ tự tăng dần của góc tạo bởi $\vec{OP}$ và $\vec{OI}$ với $I$ là một điểm nằm trên trục hoành và $\vec{OI}$ cùng hướng với chiều dương của trục hoành. Do lúc này ta không biết điểm nào sẽ là đỉnh của bao lồi nên ta đặt $h = 0$. Ta xét các điểm theo thứ tự ta vừa sắp xếp, với mỗi điểm ta sửa lại bao lồi $H$. Gọi điểm đầu tiên được cho vào bao lồi $H$ là $H_1$, điểm cuối cùng là $H_h$. Khi xét mỗi điểm ta làm như sau:

1. Thêm điểm $P$ vào cuối bao lồi $H$. Tức là ta tăng $h$ lên 1 và đặt $H_h = P$.

2. Nếu $h<3$, xét tiếp điểm tiếp theo.

3. Xét 3 điểm $H_h,H_{h-1}$ và $H_{h-2}$. Có thể sau khi cho thêm điểm $H_h$, ta biết được điểm $H_{h-1}$ chắc chắn không nằm trong bao. Gọi $\vec{u}=\overrightarrow{ H_{h-2} H_{h-1} }$ và $\vec{v}=\overrightarrow{H_{h-1} H_h}$. Nếu khi đi theo hướng $\vec{v}$ rồi đi theo hướng $\vec{u}$ là ta đã bẻ góc ngược chiều kim đồng hồ, hay $\vec{u} \times \vec{v}>0$, thì cả ba điểm đều tạm thuộc bao, và ta xét tiếp điểm tiếp theo. Nhưng nếu $\vec{u} \times \vec{v}<0$, thì góc $\widehat{H_{h-2} H_{h-1} H_{h} }$ sẽ tạo ra đa giác lõm và điểm $H_{h-1}$ phải bị loại bỏ, có nghĩa là $H_{h-1}$ được đặt là $H_{h}$ và $h$ giảm đi 1. Sau đó quay lại bước 2 cho đến khi xét hết các điểm.

Đến lúc này ta đã có một tập điểm $H_1, H_2,..., H_h$ sắp xếp ngược chiều kim đồng hồ. Vấn đề là ta chưa chắc điểm $H_1$ đã thuộc bao hay không (chú ý rằng điểm $H_1$ không thể bị loại bỏ trong các bước trên). Ngoài ra, vì bao lồi là một đường khép kín chứ không phải là một đường gấp khúc nên cũng có khả năng điểm $H_h$ không thuộc bao (điểm $H_h$ cũng không thể bị loại bỏ trong các bước trên). Cách mà chúng ta loại bỏ điểm không thuộc bao là xét 3 điểm liên tiếp trong bao, và ta cũng phải làm tương tự với hai điểm $H_1$ và $H_h$.

1. Xét 3 điểm $H_2, H_1, H_h$. Gọi $\vec{u}=\overrightarrow{H_h H_1}$ và $\vec{v}=\overrightarrow{H_1 H_2}$. Nếu $\vec{u} \times \vec{v} <0$ thì $H_1$ phải bị loại khỏi bao.

2. Xét 3 điểm $H_1, H_h, H_{h-1}$. Gọi $\vec{u}=\overrightarrow{H_{h-1} H_h}$ và $\vec{v}=\overrightarrow{H_h H_1}$. Nếu $\vec{u} \times \vec{v} <0$ thì $H_h$ phải bị loại khỏi bao.

3. Nếu không có điểm nào bị loại khỏi bao, ta đã tìm được bao lồi thật sự $H$ với các điểm được liệt kê theo thứ tự ngược chiều kim đồng hồ, nếu không thì ta quay lại bước 1.

Để đảm bảo ta có thể loại bỏ điểm $H_1$ với độ phức tạp $O(1)$ (tức là điểm $H_2$ cũ trở thành điểm $H_1$ mới,...), ta nên dùng cấu trúc dữ liệu [hàng đợi hai đầu](http://vnoi.info/algo/data-structures/data-structures-overview#1-ctdl-l%C6%B0u-tr%E1%BB%AF_1-2-stack-queue-deque) (deque) hoặc [danh sách liên kết](http://vnoi.info/algo/data-structures/data-structures-overview#1-ctdl-l%C6%B0u-tr%E1%BB%AF_1-1-m%E1%BA%A3ng-array-danh-s%C3%A1ch-li%C3%AAn-k%E1%BA%BFt-linked-list) (linked list).

Về độ phức tạp của thuật toán, ta thấy bước sắp xếp các điểm có độ phức tạp $O(n \log{n})$. Mỗi điểm được cho vào bao nhiều nhất một lần nên tổng độ phức tạp của các bước thêm điểm là $O(n)$, và mỗi điểm bị loại ra khỏi bao nhiều nhất một lần nên tổng độ phức tạp của các bước xóa điểm là $O(n)$, do đó độ phức tạp của bước xét các điểm là $O(n)$. Vậy, độ phức tạp của thuật toán Graham là $O(n \log{n})$, phù hợp cho hầu hết các bài toán. 
