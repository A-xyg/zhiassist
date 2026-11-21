"""测试生成器分块读取"""
from common.utils.chunker import read_chunks


def test_chunks_join_back_to_original(tmp_path):
    """分块拼回去应与原文一致(tmp_path是pytest提供的临时目录fixture)"""
    p = tmp_path / "sample.txt"         #在临时目录创建测试文件
    p.write_text("abcdefghij",encoding="UTF-8") #10个字符
    chunks = list(read_chunks(str(p),chunk_size=3)) #每块3字符 ==>4块
    assert chunks == ["abc","def","ghi","j"]    #断言分块正确
    assert "".join(chunks) == "abcdefghij"     #断言无丢失